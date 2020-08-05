##### IF STATEMENT #####

if 5 > 2:
 print("Five is greater than two!")  #correct usage

# if 5 > 2:
#         print("Five is greater than two!") --> also correct usage

# if 5 > 2:
# print("Five is greater than two!")  
# The number of spaces is up to you as a programmer, but it has to be at least one.

# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!") 
# You have to use the same number of spaces in the same block of code

##### PYTHON VARIABLES #####

x = 5   # x is of type int
y = "John"  # y is of type str
z = "Hello, World!" # also z is of type str
print(x)
print(y)
print(z)
# Python has no command for declaring a variable.

a = "John"
# is the same as
a = 'John'
# String variables can be declared either by using single or double quotes

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Python allows you to assign values to multiple variables in one line

x = y = z = "Orange"
print(x)
print(y)
print(z)
# And you can assign the same value to multiple variables in one line

x = "awesome"
print("Python is " + x)
# To combine both text and a variable, Python uses the + character

x = "Python is "
y = "awesome"
z =  x + y
print(z)
# You can also use the + character to add a variable to another variable

x = 5
y = 10
print(x + y)
# For numbers, the + character works as a mathematical operator

x = 5
y = "John"
print(x + y)
# ERROR

# x = "awesome"
# def myfunc():
#   print("Python is " + x)
# myfunc()
# # x is global variable 

x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)   #prints fantastic
# myfunc()
# print("Python is " + x) #prints awesome

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x) 

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) # Python is fantastic.


##### COMMENTS #####

#This is a comment.

"""
This is a comment
written in
more than just one line
"""

