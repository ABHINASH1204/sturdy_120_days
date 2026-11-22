"""Task: Student Information Program

Your program should:
1. Ask the user's name.
2. Ask the user's age.
3. Ask the user's college name.
4. Ask the user's percentage.
5. Display all information."""

"""
name = input("Enter your name:")
age = int(input("Enter your age:"))
college = input("Enter your college name:")
percentage = float(input("Enter your percentage:"))

print("\n-----student information ------")
print("name:", name)
print("age:", age)
print("college:", college)
print("percentage:", percentage)
"""


#Take your name, age and college name as input and display them.


name = input("Enter your name:")
age = int(input("Enter your age: "))
college = input("Enter your college name:")

print("\n----student info----")

print("Name:", name)
print("Age:", age)
print("college:", college)

#Take two numbers and print their sum, difference, multiplication and division.

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

sum = num1 + num2
difference = num1 - num2
multiplication = num1 * num2
division = num1/num2

print("\n----results----")
print("Sum:", sum)
print("Difference:", difference)
print("Multiplication:", multiplication)
print("Division:", division)

#Take three subject marks and calculate the average.

mark1 = float(input("Enter makes of the 1st subject :"))
mark2 = float(input("Enter makes of the 2nd subject :"))
mark3 = float(input("Enter makes of the 3rd subject :"))

average = (mark1 + mark2 + mark3)/3
print("\n----average marks----")
print("Average marks:", average)


#Convert Celsius temperature into Fahrenheit.

celsius = float(input("Enter temp in celsius:"))
Fahrenheight = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", Fahrenheight)


#Calculate simple interest using principal, rate and time

principal = float(input("Enter principal amount:"))
rate = float(input("Enter rate of interest:"))
time = float(input("Enter time :"))

simple_interest = (principal * rate * time)/100
print("Simple interest: ", simple_interest)

#Create a shopping bill using item name, quantity and price.

item_name = input("Enter item name:")
quantity = int(input("Enter quantity:"))
price = float(input("Enter price:"))

total_amount = quantity * price
print("\n------shopping bill------")
print("Item name : ", item_name)
print("Quantity:", quantity)
print("Price:", price)
