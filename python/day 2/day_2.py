"""data type 

A data type tells python what kind of variable store.

int          age = 22
float        price = 99.0
complex      x = 2 + 3j
str          name = "abhinash"
bool         is_sturdent = True
nonetype     result = None
list         marks = [90, 80, 70]
tuple        days = ("Monday", "Tuesday") 
set          numbers = {1, 2, 3}
dict         students = {"name": "abhinash"}"""


#check data type of variable

name = "Abhinash"
age = 22
height = 5.8
is_student = True
marks = [90,80,70]

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(marks))



"""type conversion
type conversion means changing the data type into another."""

a = "100"
b = int(a)

print(b)
print(type(b))


#1. Integer conversion (int())
#Changes a number into an integer.
x = 10.5
y = int(x) #converts float to integer
print(y)


#2. Float conversion (float())
#Changes a number into a decimal number.
x = 10
y = float(x) #converts integer to float
print(y)

#3. String conversion (str())
#Changes a value into text.

x = 100
y = str(x) #converts integer to string
print(y)

#4. Boolean conversion (bool())
#changes a value into true or false.

x = 1
y = bool(x) #converts integer to boolean
print(y)
 
 
 #Complete program using all four types
 
 #tsking user input and converting it into different data types.
""" 
name = str(input("Enter your name :"))
age = int(input("Enter your age :"))
height = float(input("Enter your height:"))
is_student = input("Are you a student? ").lower() =="yes"

#display the information 
print("\n----- data type -----") 

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))"""
 
#user input 
"""name = input("enter your name:")
print("hello", name)
age = input("enter your age:")
print(type(age))
age = int(input("enter your age:"))
print(age + 5)
"""
#output formatting
# f string is used to format the output in python. It allows you to embed expressions inside string literals, using curly braces {}.
 
name = "Abhinash"
age = 22
print (f"my name is {name} and my age is {age} years old")
print("Python", "Java", "SQL", sep=" | ")
