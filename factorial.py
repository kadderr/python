number = int(input("Please enter the number to be calculated by factor: "))
factorial = 1
counter = 1
while number+1 > counter:
    factorial *= counter
    counter += 1
print(factorial)

