# <!-- what is python?

# it is an hight level general purpose , interpreted  programming language created by Guido van Rossum.

# -> in 1991  -->


print("Hello world")


# python is a open source code is publicly available and developer can use sturdy modify abd distribute it under its licence.


a = 10
b = 20

print(a + b)

# oop organizes code into objects and classes.


class Student:
    def study(self):
        print("student is studying")
        
s1 = Student()
s1.study()


# python can be used for web development, data analysis, artificial intelligence, scientific computing, and more. It has a large standard library and a vibrant community that contributes to its growth and development.


# intro code for python programming language.

print("HEllo world ")
print ("my name is abhinash")
print(" im learning programming")

#Python syntax = Syntax means the rules used to write valid Python programs.


# indentation means spaces at the beginning of a line 

# python use indentation to define code blocks 

if 10 > 5:
    print("10 is greater")


""" Variable is a name that refers to an object/value in memory"""

""" Assigning multiple variable """

name,age,city = "abhinash", 22, "bbsr"
print(name)
print(age)
print(city)

#i can also do this 
a = b = c = 100
print(a,b,c)


#check variable types 

name = "abjinash"
age = 22
height = 5.8

print(type(name))
print(type(age))
print(type(height))