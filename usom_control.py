from tkinter import *
import datetime

def check_it():
    file = open("usom.txt", "r")
    txt_content = file.read()
    file.close()
    ip = entry1.get()
    today = datetime.datetime.now()
    if str(ip) in txt_content:
        file = open("log.txt", "a")
        article = str(ip)+" is harmful\nDate: "+str(today)+"\n"
        file.write(article)
        file.close()
        var.set("IP is harmful!")
    else:
        file = open("log.txt", "a")
        article = str(ip) + " is not harmful\nDate: "+str(today)+"\n"
        file.write(article)
        file.close()
        var.set("IP is not harmful!")
top = Tk()
top.title("USOM IP CONTROL")
B = Button(top, text="CHECK", command=check_it)
B.place(x=50, y=50)
B.pack()
label1 = Label(top, text="Please enter the IP address to be checked.")
label1.place(x=50, y=80)
label1.pack()
entry1 = Entry(top)
entry1.place(x=50, y=90)
entry1.pack()
var = StringVar()
entry2 = Entry(top, textvariable=var)
entry2.place(x=50, y=100)
entry2.pack()
top.mainloop()
###
