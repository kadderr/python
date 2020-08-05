def even_function(number):
    list = []
    for i in range(0,number,1):
        if i%2 == 0:
            list.append(i)
    return list