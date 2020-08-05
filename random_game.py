import random
random_number = round(random.random()*100)
# round(random.random()) 0-1 arasinda rand sayi uretir.
# round(random.random()*100) 0-100 arasında rand sayi uretir.
#print(random_number)
input_number = int(input("Please enter a number between 0 and 100 : "))
while random_number != input_number:
    if input_number > random_number:
        print("Please enter a smaller number : ")
    else:
        print("Please enter a bigger number : ")
    input_number = int(input("Please enter a number between 0 and 100 : "))
print("Congratulations! You found the right number.")
print("The number was " + str(input_number))