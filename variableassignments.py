#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Take the input from the user for(Total number of people, Number of seats for bus. Based on two inputs 
#Decide how many number of buses required 
p=int(input())
s=int(input())
b=p//s 
if ((p%s)!=0):
    print(b+1)
else:
    print(b)


# In[ ]:


#2.take temperature from the user and convert foreign heat -> Celsius. 
F=int(input())
celsius=(F-32)*(5/9)
print(str(celsius)+"C")


# In[ ]:


#3.take temperature from the user and convert Celsius → foreign heat.
c=int(input())
Foreign_heat=(9*c/5)+32
print(str(Foreign_heat)+"F")


# In[7]:


#4.
a,b,c,d = map(int,input().split())
res1 = (a+b)**2
res2 = (c+d)**3
mean = (a+b+c+d)/4
varience = ((a-mean)**2 + (b-mean)**2 + (c-mean)**2 + (d-mean)**2)/4
std_dev = (varience)**(0.5)
y = 1.23*(a+b+c+d)+0.045
avg = mean
sum_of_four = a+b+c+d
print(res1)
print(res2)
print(varience)
print(std_dev)
print(y)
print(avg)
print(sum_of_four)


# In[ ]:


#5.Take the distance in km  Show that in cm, meters, in milli meters, cents, feets, yards 
km=int(input())
m=km*1000
cm=km*1000*100
mm=km*1000*1000
cents=40.4686*(m*m)
feet=(0.002296169)**0.5
yards=3*feet
print(str(m)+"m")
print(str(cm)+"cm")
print(str(mm)+"mm")
print(str(cents)+"cents")
print(str(feet)+"feet")
print(str(yards)+"yards")


# In[ ]:


#6.Take the size of your hard disk in GB Show that in MB, KB, TB, PB 
GB=int(input())
MB=GB/1000
KB=MB/1000
TB=GB*1000
PB=TB*1000
print(MB)
print(KB)
print(TB)
print(PB)


# In[ ]:


'''' #7.Take name, age, height from the user and print like below 

The details of the person: Name:name of the person, Age:age of the person, Height:height of the person 

Note: make sure that no space between : and a value and should be space after “COMA” 
''''

name=input()
age=int(input())
height=int(input())
print("name:"+name)
print("Age:"+str(age))
print("height:"+str(height))


# In[ ]:


#8.BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person. 
weight=int(input())
height=int(input())
BMI=weight/height
print(BMI)


# In[11]:


'''9.. name="Jayaram" 

age=1.6 

height=3.5356234 

weight=10.343856783 

By using above inputs print the output 

Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344 

Note: Use format specifiers(%s, %d, %f) 
'''
name=input()
age=float(input())
height=float(input())
weight=float(input())
info = "Name: %s, Age: %f, Height: %f, Weight: %f"%(name, age, height, weight)
print(info)


# In[ ]:


#10.Take three upper case letters from the user convert in to small case.
a=input()
b=a.lower()
print(b)


# In[ ]:


#11. take base and exponent value from the user and print like in mathematics: example: base=2, exponent=3: 23 
base=int(input())
exponent=int(input())
print(base**exponent)


# In[ ]:


#12.Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost. 
a=list(map(int,input().split()))
b=len(a)
print(sum(a))
print(sum(a)/b)
print(max(a))
print(min(a))


# In[ ]:


##13Assign “ten” value to variable it is 10 otherwise assign “Not ten”  Note: write two versions of program  Version1: use and operator  Version2: use or operator  
a=int(input())
if a==0:
    print(a or 10 )
else:
    print("Not ten"


# In[ ]:


a=int(input())
if a!=0:
    print(a and 10)
else:
    print("Not ten")


# In[1]:


#13 conditional statements Take the input from the user for(Total number of people, total number of buses, Number of seats for bus, adjust factor). Based on four inputs 

#Decide whether there is sufficient buses or not and give solution for how many extra buses required. 
total_no_of_people=int(input("enter total_no_of_people"))
total_no_of_buses=int(input("enter total_no_of_buses"))
no_of_seats_per_bus=int(input("no_of_seats_per_bus"))
adjust_factor=int(input("enter adjust factor"))
total_no_of_seats=total_no_of_buses*no_of_seats_per_bus 
remaining_people=(total_no_of_people)-(total_no_of_seats)
update_adjust_factor=(remaining_people)-(adjust_factor)
if update_adjust_factor>0:
    print(f'required_sufficient_buses =  {round(update_adjust_factor/no_of_seats_per_bus)}')
else:
    print("sufficient_buses")



# In[ ]:


#14 Take number from the user decide whether it is even or odd. 
a=int(input())
if a%2==0:
    print("Even")
else:
    print("Odd")


# In[ ]:


#15 take number from the user decide whether it is positive number or negative number 
a=int(input())
if a>=0:
    print("positive")
else:
    print("Negative")


# In[ ]:


#16 take a string from the user print the length. if the user not given anything then show an error message 
a=input()
if a!="":
    print(len(a))
else:
    print("Error message")


# In[10]:


'''''17code to perform mathematical operations. take two numbers from the user and show the below menu 

1. add, 

2. sub,	 

3. mul, 

 	4.div,  

5.quit 

Enter an option: 

based on the option need to perform an operations 
''''
a=int(input())
b=int(input())
c=int(input("enter an option for add=1,sub=2,mul=3,div=4,quit=5"))
if c==1:
    print(a+b)
if c==2:    
    print(abs(a-b))
if c==3:
    print(a*b)
if c==4:
    print(a/b)
if c==5:
    print("quit")
    


# In[ ]:


'''''18. show the menu: 

   		 1. kids 

    		2. Men's 

   		 3. Women's 

    		Show the corresponding message based on the selection. 

Option:1: you are a kid 

                                           2: you are a gentlemen 

                                            3: you are a good women 

 

 Mention error message if the option value >3. 
''''
print("enter below options\n 1.kids\n 2.Men's\n 3.women's")
a=int(input())
if a==1:
    print("you are a kid")
if a==2:
    print("you are a gentlemen")
if a==3:
    print("you are a good women")


# In[ ]:


'''' 19.write a program to chcek given substring is there in actual string or not? 

example: act="python is a pure object oriented programing language" 

check whether “pure” is there in act or not. 

Note: Use in operator 
''''
a=input()
b=input()
if b in a:
    print("string is there")
else:
    print("string is not there")


# In[4]:


#20 Take three numbers from the user and decide which is big 
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
if b>a and b>c:
    print(b)
if c>a and c>b:
    print(c)


# In[5]:


#21 Take age and gender from the user and decide whether he is eligible for 	marriage in India or not. Age criteria: men age>24, women>21 
age=int(input())
gender=input()
if (gender=="men" and age>24) or (gender=="women" and age>21):
    print("eligible for marriage")
else:
    print("not eligible for marriage")


# In[11]:


''''' Take an age  and gender from the user: and mention that what he/she can 	do in india. 

""" 

conditions 

1. Theatre: 5 for men 7 for women 

    	2. Voting system: 18 for men and women 

    	3. Marriage in india: 23 for men and for women >21 

    	4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for 	women 

   	 5. For driving licence: (min:18, max:60) for men and women 

Eligibility: 

   		1. theatre 

2.  Voting system 

3.  Marriage in india 

4.  For govt obs 

5. For driving licence: 

Enter an option: 

Gender: 

1. men 

2. women 

Enter an option: 

Enter an age of person: 
'''
gender=input("enter gender:\n 1.men\n 2.women\n")
age=int(input("enter age\n"))
if (gender=="1" and age>=5) or (gender=="2" and age>=7):
    print("eligible for Theatre")
if (gender=="1" and age>=18) or (gender=="2" and age>=18):
    print("eligible for Voting system")
if (gender=="1" and age>=23) or (gender=="2" and age>=21):
    print("eligible for marriage")
if (gender=="1" and ((age>=18) and (age<=32))) or (gender=="2" and ((age>=18) and (age<=34))):
    print("eligible for government jobs")
if (gender=="1" or gender=="2") and ((age>=18) and (age<=60)):
    print("eligible for Theatre")    


# In[13]:


''''operating systems: 

1.windows 

2.android 

3.mac 

Enter an option: 

 

If the user enters 1 then show "Goto first floor and buy windows laptop or mobile" 

If the user enters 2 then show "Goto second floor and buy adroid mobiles" 

If the user enters 3 then show "Goto third floor and buy mac laptop or iphones" 

If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3" 
''''
user=int(input("enter below options \n 1.windows\n 2.android \n 3.mac \n"))
if user==1:
    print("Goto first floor and buy windows laptop or mobile")
if user==2:
    print("Goto second floor and buy android mobiles")
if user==3:
    print("Goto third floor and buy mac laptop or iphones")
if user>3:
    print("There is only three floors,please select 1 or 2 or 3")


# In[14]:


#24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger. 
age = int(input("Enter your age \n"))
if age <= 1:
    print("baby")
elif age > 1 and age <=5:
    print("toddler")
elif age > 5 and age <=12:
    print("child")
elif age > 13 and age <= 19:
    print("teenage")
elif age > 20 and age <= 34:
    print("adult")
elif age >= 60:
    print("old codger")
else:
    print("Younger")


# In[23]:


#25 Take two number a,b from the user and check whether a is divisible by b or not 
a=int(input())
b=int(input())
if b!=0:
    if ((a%b==0)):
        print("a is divisible by b")
    else:
        print("a is not divisible by b")
else:
    print("Zero division error")


# In[29]:


#26Take a letter from the user and print that letter belongs to which category
#I.e is it a small letter or capital letter or number or special symbol 
s=input("enter one letter\n")
if s.isdigit():
    print("it is a number")
elif s.islower():
    print("it is a small letter")
elif s.isupper():
    print("it is a capital letter")
else:
    print("it is a Special symbol")


# In[6]:


#25 looping statements take a number from the user and check whether it is prime? 
n=int(input())
factors=0
for i in range(2,n):
    if (n%i==0):
        factors=factors+1
if factors==0 and (n!=1 and n!=0):
    print("prime")
else:
    print("not prime")
    


# In[10]:


#26.take a string from the user and check contains only digits or not? 
a=input()
if a.isdigit():
    print("true")
else:
    print("False")


# In[15]:


#27take a string from the user and check contains only  alphabets or not? 
a=input()
b=""
for i in a:
    if ((i>="a" or i>="A") and (i<="z" or i>="Z")):
        b=b+i
if len(a)==len(b):
    print("True")
else:
    print("False")


# In[26]:


#28 take a string from the user and check contains only  special chars or not? 
a=input()
c=0
for i in a:
    if not i.isalnum():
        c=c+1 
if c==len(a):
    print("True")
else:
    print("False")


# In[30]:


#29.Take a string from the user and check contains only capital letters or not?
a=input()
b=0
for i in a:
    if i.isupper():
        b=b+1
if b==len(a):
    print("True")
else:
    print("False")


# In[32]:


# 30.Take a string from the user and check contains only small letters or not?
a=input()
b=0
for i in a:
    if i.islower():
        b=b+1 
if b==len(a):
    print("True")
else:
    print("False")


# In[7]:


'''
31. WAP to replace last n occurrence of give string.
For example:”apple,orange,apple,grape,orange,apple,apple,orange”
source: “apple”
last occurrences: 2
replace with: APPLE
output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange”
'''
a=input()
b=input()
c=int(input())
d=input()
e=a.rsplit(b,c)
f=d.join(e)
print(f)



# In[13]:


#32 WAP to check given string contains numbers or not. it should consider float numbers also.
a=input()
c=0
if a.isdigit() or a.count("."):
    c=c+1
if c>=1:
    print("True")
else:
    print("False")


# In[25]:


#33   Convert the total string in to lower case. Without using lower() function.
s=input()
b=s.upper()
result=""
for i in b:
    a=int(ord(i))+32
    result=result+chr(a)
print(result)


# In[ ]:


#34   Convert the total string in to upper case. Without using upper() function.
s=input()
b=s.lower()
result=""
for i in b:
    a=int(ord(i))-32
    result=result+chr(a)
print(result)


# In[1]:


'''35Show the below menu to the user until and until user select quit and display corresponding os message
      Menu:

        1. windows
        2. Linux
        3. Mac
        4. quit
'''       
while True:
    a=input("enter below options \n 1.windows \n 2.Linux \n 3.Mac \n 4.quit \n ")
    if a=="1":
        print("windows")
    elif a=="2":
        print("Linux")
    elif a=="3":
        print("Mac")
    if a=="4":
        print("quit")
        break


# In[2]:


#36 Take a string from the user and check contains at least one digit or not?
s=input()
c=0
for i in s:
    if i.isdigit():
        c=c+1
if c>=1:
    print("string contains digit")
else:
    print("string does not contain digit")
    


# In[5]:


#37. take a string from the user and check contains at least one alphabets or not?
a=input()
c=0
for i in a:
    if i.isalpha():
        c=c+1
if c>=1:
    print("string contains alphabets")
else:
    print("String does not contains alphabets")


# In[4]:


#38 take a string from the user and check contains at least one chars or not? 
a=input()
if len(a)==0:
    print("String has no characters")
else:
    print("String has characters")
    


# In[7]:


#39 take a string from the user and check contains at least one capital letter or not? 
a=input()
count=0
for i in a:
    if (i>="A" and i<="Z"):
        count=count+1
if count>=1:
    print("yes the string contains capital letter")
else:
    print("the string does not contain capital letter")


# In[9]:


#40take a string from the user and check contains at least one small letter or not?
a=input()
count=0
for i in a:
    if (i>="a" and i<="z"):
        count=count+1
if count>=1:
    print("yes the string contains small letter")
else:
    print("the string does not contain small letter")


# In[18]:


#41  Print the first 100 odd numbers 
result=""
for i in range(1,200):
    if ((i%2)!=0):
        result=result+str(i)+" "
print(result)        


# In[17]:


#42 Determine the factors of a number entered  by the user 
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)


# In[35]:


#43 Play a number guessing game (User enters a guess, you print YES or Higher or Lower).
#This should continue until and until user gives a correct number or want to quit in the middle. 
import random
a=random.randint(1,100)
while True:
    n=(input("enter number\n"))
    if n=="q":
        print("the correct answer is:"+str(a))
        break
    elif n==str(a):
        print("you have guess a correct number")
    elif n<str(a):
        print("please enter higher number")
    elif n>str(a):
        print("please enter lower number")


# In[2]:


#44.Take two numbers from the user a,b check whether a is divisible by b or not? 
a=int(input())
b=int(input())
if a%b==0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")
    


# In[3]:


#45.Find the sum of all the multiples of 3 or 5 below 1000 
sum=0
for i in range(1,1000):
    if (i%3==0) or (i%5==0):
        sum=sum+i
print(sum)        


# In[4]:


#46.Write a program to find out big of two numbers 
a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)


# In[6]:


#47. Write a program to find out biggest number in the given numbers. 
n=list(map(int,input().split()))
print(max(n))


# In[12]:


#48. find out the index of  third occurrence of given substring (apple apple orange guava apple,apple,output 5)
sentence=input().split()
substring=input()
count=0
for i in range(len(sentence)):
    if sentence[i]==substring:
        count=count+1
        if count==3:
            print(i)
            break


# In[23]:


#49.find out the index nth occurrence of given substring 
sentence=input().split()
substring=input()
count=0
for i in range(len(sentence)):
    if sentence[i]==substring:
        count=count+1
        result=i
print(result)        


# In[28]:


#50.Take some single digit numbers from the user and findout min, maximum, sum, average 
n=list(map(int,input().split()))
print(min(n))
print(max(n))
sum=0
for i in n:
    sum=sum+i
print(sum)
print(sum/len(n))


# In[38]:


'''51. print the number in proper mathematical way. 

Consider that we have 6 digit numbers. 

Number format  WAP> 10 -> 000010 

       		100 ->  000100 

      		1000 ->  001000 

 		 2345678  ->  2345678 

If the number has more than 6 digits then print as it is. 
'''
a=input()
b=len(a)
c=6-b
if b==6:
    print(a)
else:
    d="0"*int(c)
    print(d+str(a))
    


# In[39]:


#52. names  ="emp1,emp2,emp3,emp4" iterate through the employee names. 
a=input().split(",")
for i in a:
    print(i)
    


# In[ ]:


#53. Take actual string, source string, destination string. 
#replace first nth occurrences of source string with destination string of actual string. 
actual_string=input().split()
source_string=input()
destination_string=input()
count=0
for i in range(len(actual_string)):
    if source_string[i]==actual_string:
        count=count+1
        result=i 
        


# In[ ]:


#54

