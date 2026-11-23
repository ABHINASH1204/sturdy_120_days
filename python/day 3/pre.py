#1. Take two numbers and perform all seven arithmetic operations.
a = 20
b = 10

print("Addition :", a + b)
print("Subtract :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("modulus :", a % b)
print("Exponent :", a ** 2)

#2. Check whether a number is even or odd using modulus.

num = int(input("Enter the number:"))
print("Even:", num % 2==0)


#3. Check whether a person is eligible to vote (age >= 18).

age = int(input("Enter your age:"))
print("eligible:", age >= 18)

#4. Take three numbers and check whether all are greater than 10.

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
if num1 > 10 and num2 >10 and num3 > 10:
    print("All three number is greater then 10")
else:
    print("All three number is smaller then 10")
    
    
#5. Calculate the final price after a user-entered discount.

price = float(input("Enter the price:"))
Discount = float(input("Enter the discount price:"))

final_price = price * (price * Discount / 100)
print("final_price :", final_price)