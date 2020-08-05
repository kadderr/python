# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview

# You can get the data type of any object by using the type() function.

x = 5
print(type(x))  #prints <class 'int'>

x = "Hello World"   #str
x = 20  #int
x = 20.5    #float
x = 1j  #complex    #print(x) : 1j	
x = ["apple", "banana", "cherry"] 	#list 	
x = ("apple", "banana", "cherry") 	#tuple 	
x = range(6) 	#range 	
x = {"name" : "John", "age" : 36} 	#dict 	
x = {"apple", "banana", "cherry"} 	#set 	
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset 	
x = True 	#bool 	
x = bytes(5) 	#bytes  #print(x) : b'\x00\x00\x00\x00\x00'	
x = bytearray(5) 	#bytearray #print(x) :	bytearray(b'\x00\x00\x00\x00\x00')
x = memoryview(bytes(5)) 	#memoryview #print(x) : <memory at 0x006F8FA0>

