import os
import time
import requests
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.sedarplus.ca/csa-party/service/create.html?targetAppCode=csa-party&service=searchDocuments&_locale=en"
PDF_FOLDER = "pdf"
os.makedirs(PDF_FOLDER, exist_ok=True)

driver = webdriver.Chrome()
driver.get(BASE_URL)
wait = WebDriverWait(driver, 10)

def extract_data():
    soup = BeautifulSoup(driver.page_source, "html.parser")
    rows = soup.select("table tbody tr")
    data = []
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 6:
            profile = columns[0].get_text(strip=True)
            document = columns[1].get_text(strip=True)
            submitted_date = columns[2].get_text(strip=True)
            principal_jurisdiction = columns[3].get_text(strip=True)
            file_size = columns[4].get_text(strip=True)
            try:
                link_element = driver.find_element(By.XPATH, "//td[6]/a")
                pdf_link = link_element.get_attribute("href")
                if pdf_link == "#" or not pdf_link:
                    pdf_link = None
                elif not pdf_link.startswith("http"):
                    pdf_link = urljoin(BASE_URL, pdf_link)
            except Exception as e:
                pdf_link = None
            data.append({
                "Profile": profile,
                "Document": document,
                "Submitted Date": submitted_date,
                "Principal Jurisdiction": principal_jurisdiction,
                "File Size": file_size,
                "PDF Link": pdf_link
            })
            if pdf_link:
                download_pdf(pdf_link, document)
    return data

def download_pdf(pdf_url, document_name):
    pdf_name = f"{document_name}.pdf".replace("/", "_").replace("\\", "_")
    file_path = os.path.join(PDF_FOLDER, pdf_name)
    try:
        response = requests.get(pdf_url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as pdf_file:
                pdf_file.write(response.content)
    except Exception as e:
        pass

all_data = []
while True:
    page_data = extract_data()
    all_data.extend(page_data)
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Next")))
        next_button.click()
        time.sleep(3)
    except Exception:
        break

csv_path = "scraped_data.csv"
df = pd.DataFrame(all_data)
df.to_csv(csv_path, index=False)

json_path = "scraped_data.json"
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(all_data, json_file, indent=4)

driver.quit()
