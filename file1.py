for i in range (1,10,1):
    file = open("numbers.txt", "a") #a means append mode
    data = str(i) + "\n"
    file.write(data)
    file.close()
# code creates numbers.txt file