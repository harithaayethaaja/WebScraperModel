# Web Scraping Project

## Overview

This project is a web scraping application that extracts documents and related data from a public service website. The data includes profiles, submission dates, file sizes, and PDF links. The script uses Selenium for dynamic content handling, BeautifulSoup for HTML parsing, and Requests for downloading PDFs. The extracted data is saved in both CSV and JSON formats, and the PDFs are stored in a local directory.

## Approach

1. **Selenium** is used to interact with the website and retrieve dynamic content, such as links and text from the table.
2. **BeautifulSoup** is used to parse the HTML and extract relevant data from the page.
3. **Requests** is used to download PDF files linked in the extracted data.
4. Data is saved in **CSV** and **JSON** formats for easy analysis.
5. The script handles pagination to ensure all pages are scraped.
6. PDFs are saved in a local folder named `pdf`.

## Installation

Before running the script, make sure you have all the dependencies installed.

1. Clone or download the project files.
2. Install Python 3.x and make sure it's added to your PATH.
3. Create a virtual environment (recommended but optional):
   ```bash
   python -m venv venv

4. Install the required dependencies:
    bash
    Copy code
    pip install -r requirements.txt

5. 

    1. Running the Script
    Make sure you have Chrome installed, as this script uses ChromeDriver for Selenium. You can download it here and ensure the version matches your browser.

    2. Run the script using Python:
        python scripts.py

    3. The script will automatically start scraping the data, downloading the PDFs, and saving the data in both CSV and JSON formats.

OUTPUT:

    Data will be saved in a CSV file: scraped_data.csv
    Data will also be saved in a JSON file: scraped_data.json
    PDFs will be stored in a local folder named pdf.

Conclusion:

This script successfully scrapes data from the target website and downloads related PDF files. It provides the flexibility to extract data from multiple pages and store it in CSV and JSON formats for easy analysis. The challenges related to dynamic content and pagination were addressed by using Selenium effectively.