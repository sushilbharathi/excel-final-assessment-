# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JWnSWmJiCY1I6NAk5NuUnSQsiYTIrbQv
"""

## 1
length=int(input("enter the length of the rectanlge: "))
width=int(input("enter the width of the rectanlge:"))
area=length*width
print(area)

## 2
weight=int(input("enter your weight in (kgs) : "))
height=int(input("enter your height in (m):"))
bmi=weight/(height*height)
print(bmi)

## 3
students={}
i="yes"
while(i.lower()!="done"):
  student=(input("enter the students name: "))
  score=(input("enter their score: "))
  students[student]=score
  i=input("enter yes if you want ot insert more data or enter done ")
print(students)

## 4
age=int(input("please enter your age: "))
if age<18:
  print("you are a minor")
elif age>=18 and age<40:
  print("you are an adult")
else :
  print("you are a senior ")

## 5
for i in range(2,50,2):
  print(i)

## 6
password={"sushil":"123456","shakti":"1234567","ashis":"12345678"}
name=(input("enter the user name: "))
passwords=input("please enter the password: ")
while 1:
  if passwords==password[name]:
    break
  passwords=input("please enter the password: ")

print("you have logged in")

## 7
import math
def average_numbers(numbers):
  a=sum(numbers)
  return a/len(numbers)

number=[]
i="yes"
while i!="done":
  n=int(input("enter the numbers: "))
  number.append(n)
  i=input("enter yes to continue or enter done: ")
print(average_numbers(number))

## 8
def vowels(chars):
  a=0
  for i in chars.lower():
    if i in ("a","e","i","o","u"):
      a+=1
  return a
char=input("enter the string: ")
print(vowels(char))

## 9

import datetime
def todays():
  today = datetime.datetime.now()
  return today
print(todays())

## 10
try:
  value=int(input("enter the value: "))
  value2=int(input("enter another value: "))
  print(value=value2)
except :
  print("enter numeric value")

##11
try:
  value=int(input("enter any value: " ))
  print(value)
except :
  print("enter only whole number:")

## 12
try:
  a = int(input("enter the first value for division: "))
  b= int(input("enter the second value for division: "))
  print(a/b)

except:
  print("do not enter zero in the second value")

## 13
file_create=open("/content/sample_data/anscombe.json","w")
file_input=["hello python"]
file_create.writelines(file_input)
file_create.close()

## 14
file_create=open("/content/sample_data/california_housing_train.csv","r")
for i in range(5):
  a=file_create.read()
  print(a)

file_create.close()

## 15
file_create=open("/content/sample_data/anscombe.json","w")
file_input=["the file is empty"]
file_create.writelines(file_input)
file_create.close()
file_create=open("/content/sample_data/anscombe.json","r")
a=file_create.read()
print(a)
file_create.close()