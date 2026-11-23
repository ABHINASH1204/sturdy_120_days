#Python Operators and Expressions
 
""" what are operators
An operator is a symbol that performs an operation on values or variable
"""
a = 10
b = 20
print(a+b)

"""     
+ = addition 
- = subtract 
* = multiplication
/ = division
// = floor division
% = modulus (remainder)
** = exponent"""

print(10/3)
print(10//3)
print(10%3)


#practice 1 

a = 20
b = 2

print("Addition:", a + b)
print("Subtraction:",  a- b)
print("Multiplication:", a * b)
print("Divide:",  a/b)
print("Floor Division: ", a // b)
print("Reminder:", a % b)
print("Power:", a**b )





"""  
Comparison operators
==   equal to
!=   not equal to
>    Greater than
<    less than
>=   greater than equal to
<=   less then equal to 
"""

a = 20
b = 10

print( a==b )
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)

""" 
= assign a value
== compare to values
"""

age = 22
print(age == 22)


""" 
Logical Operators
and  = true when both conditions are true
or  = true when at least onr condition is true
not  = reverses the result
"""
# AND example
age = 15
print(age >= 19 or age <= 10)

# OR example
age = 16
print(age >= 18 or age <= 10) 
# it is false because both conditions are false

# NOT example

is_student = True
print(not is_student)


""" 
Assignment operators 
Assignment operators assign or update values
=     x = 10       => Assign 10
+=    x += 5       => x = x - 5
-=    x -= 5       => x = x - 5
*=    x*= 2        => x = x * 2
/=    x /= 2       => x = x / 2
//=   x //= 2      => x = x // 2
%=    x %= 3       => x = x % 3
**=   x **= 2      => x = x ** 2
"""

x = 10

x += 5
print(x) #15

x *=2
print(x)#30

x -= 10
print(x) #20


""" 
Membership operators 

this check whether an item exists inside a sequence or collection

in 
not in 

"""

name = "abhinash"
print("a" in name)
print("a" not in name)


numbers = [10,20,30,40]
print(20 in numbers)
print(50 not in numbers)



""" 
Identity operators 

identity operators check whether two variables refers to same object
is
not is
"""

a = [10,20]
b = a
c = [10,20]

print(a is b) #true
print(a is c)#false
print(a == c)# true

# important == checks whether values are equal is checks whether they are the same objects

""" 
Operator precedence 
Operator precedence determines which operation python performs first 
"""
result = 10 + 5 * 2
print(result)

#multiplication happens before addition
# use parentheses to control the order

result = (10 + 5) * 2
print(result)

