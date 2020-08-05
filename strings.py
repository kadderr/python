#'hello' is the same as "hello"

print("Hello")
print('Hello')

x = "Hello"
print(x) 

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b) 

c = "Hello, World!"
print(c[1])
# strings are arrays, prints e

d = "Hello, World!"
print(bd2:5])
#slicing prints llo

e = "Hello, World!"
print(e[-5:-2])
#Use negative indexes to start the slice from the end of the string
# prints orl 

f = "Hello, World!"
print(len(f))
#To get the length of a string, use the len() function.
#prints 13

### String Methods ###

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

"""To check if a certain phrase or character is present in a string,
we can use the keywords in or not in."""
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)    #prints TRUE

### String Concatenation ###

#To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c) # prints HelloWorld

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c) # prints Hello World

# we cannot combine strings and numbers like this
# age = 36
# txt = "My name is John, I am " + age
# print(txt)    #ERROR

# we can combine strings and numbers by using the format() method!
"""The format() method takes the passed arguments, formats them,
and places them in the string where the placeholders {} are:"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

"""The format() method takes unlimited number of arguments,
and are placed into the respective placeholders:"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

### ESCAPE CHARACTER ###

# txt = "We are the so-called "Vikings" from the north." ERROR
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# We are the so-called "Vikings" from the north.

# \' 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value #txt = "\110\145\154\154\157" prints Hello	
# \xhh 	Hex value #txt = "\x48\x65\x6c\x6c\x6f" prints Hello

### STRING METHODS ###

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	r()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle() 	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning








