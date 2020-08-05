file = open("numbers.txt", "r") #r means read
content = file.read()
file.close()
for i in content.splitlines():
    print(i)
