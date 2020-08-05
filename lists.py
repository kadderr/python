# """
# Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#     1- List is a collection which is ordered and changeable. Allows duplicate members.
#     2- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     3- Set is a collection which is unordered and unindexed. No duplicate members.
#     4- Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# """

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist)

# print(thislist[1])  #banana

# # Negative Indexing
# print(thislist[-1]) #mango

# # Range of Indexes
# print(thislist[2:5]) #['cherry', 'orange', 'kiwi']
# # Note: The search will start at index 2 (included) and end at index 5 (not included).

# print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

# print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']

# print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

# # Change Item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# # Loop Through a List
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x) 

# # Check if Item Exists
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list") 

# # List Length
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist) #['apple', 'banana', 'cherry', 'orange']


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange") #Insert an item as the second position
# print(thislist) #['apple', 'orange', 'banana', 'cherry']

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist) #['apple', 'cherry']

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist) #['apple', 'banana']

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist) #['banana', 'cherry']

# # thislist = ["apple", "banana", "cherry"]
# # del thislist 
# # print(thislist) #The del keyword can also delete the list completely

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist) #The clear() method empties the list

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

#Join Two Lists
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3) 

# # list1 = ["a", "b" , "c"]
# # list2 = [1, 2, 3]

# # for x in list2:
# #   list1.append(x)

# # print(list1) 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# The list() Constructor
# It is also possible to use the list() constructor to make a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)







