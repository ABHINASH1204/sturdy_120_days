
""" 
Practical programs 
"""
# program simple calculator 

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

print("Addition:", a + b )
print("Subtraction:", a - b)
print("Multiplication:", a * b)


# program 2 : Even or Odd

num = int(input("Enter a number:"))
print("Even:", num % 2 == 0)


# program 3 : age eligibility 

age = int(input(" Enter your age:"))
print("Eligible:", age>=18)


# program 4 : Shopping discount

price = float(input("Enter price:"))
discount = float(input("Enter discount price"))

final_price = price - (price * discount / 100)
print(f"final_price{final_price}")