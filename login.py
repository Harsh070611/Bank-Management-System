from tkinter import *
import pandas as pd
from _csv import reader
import csv
import webbrowser as wb
import tkinter.messagebox as ms

def reset():
	u_name.delete(0,END)
	u_pass.delete(0,END)
	u_email.delete(0,END)
	u_account.delete(0,END)

def submit():
	name_ = u_name.get()
	password_ = u_pass.get()
	account = u_account.get()

	i = 0
	file = open("array.csv", "r")
	csv_reader = csv. reader(file)
	a = []
	for row in csv_reader:
		a.append(row)
	while i < len(a):
	    if name_ ==  a[i][1] and password_ == (a[i][2]) and account == a[i][4]:
	        ms.showinfo("NOTIFICATION","We Have Identified You, Here is your Details of Bank Account")
	        balance_ = int(a[i][3])
	        loan = int(a[i][5])

	        f = open("det.txt","w")
	        info = name_ + " " +  account + " " + str(balance_) + " " + str(loan) + " "
	        f.write(info)
	        f.close()
	        wb.open("HOME PAGE.py")
	        break

	    i = i + 1
	    if i == len(a):
	    	ms.showinfo("INVALID CREDENTIALS", f" NO SUCH ACCOUNT EXIST WITH USERNAME  '{u_name.get()}'  TRY AGAIN")


	    
	    


root = Tk()

root.minsize(900 , 700)
root.maxsize(900,700)
root.config(bg = "#FFE0BE")
img = PhotoImage(file = "bank.png")

photo = Label(image = img, width = 900 , height = 300)
photo.pack()

l = Label(text = "Welcome To Birla Bank" , font = "arial 25 bold")
l.place(x = 300 , y = 10)

img1 = PhotoImage(file = "logo.png")

photo1 = Label(image = img1, width = 200 , height = 130 )
photo1.place(x = 310,  y = 310)

name = Label(text = "Username", fg = "red" , font = "arial 12 bold")
password = Label(text = "Password",fg = "red" , font = "arial 12 bold")
email = Label(text = "Email Id",fg = "red",font = "arial 12 bold")
account = Label(text = "ACCOUNT NO.",fg = "red",font = "arial 12 bold")
city = Label(text = "City ", fg = "red",font = "arial 12 bold")

Label(text = "' WE ARE NOT RUNNING THE BANK \n ACTUALLY YOUR  TRUST IS RUNNING THE BANK. \n HAVE A GOOD DAY.'", font = "comicssanms 15 bold italic" , fg = "blue" , bg = "#FFE0BE").place(x = 400 , y = 540)


Label(text = "USER CREDENTIALS", font = "arial 15 bold", bg = "#FFE0BE").place( x = 320 , y = 450)

name.place(x = 100 , y = 500)
password.place(x = 100 , y = 550)
email.place(x = 100 , y = 600)
account.place(x = 420 , y = 495)
city.place(x = 420, y = 545)

 
u_name = Entry(root)
u_pass = Entry(root)
u_email = Entry(root)
u_account = Entry(root)

u_name.place(x = 210 , y = 500)
u_pass.place(x = 210 , y = 550)
u_email.place(x = 210 , y = 600)
u_account.place(x = 550, y = 495)



sub = Button(text = "SUBMIT", bg = "#7DD0CC", width = 10 , height = 1 ,font = "arial 12 bold", command = submit)
res = Button(text = "RESET", bg = "#7DD0CC", width = 10 , height = 1 , font = "arial 12 bold", command = reset)

sub.place(x = 240,y = 650)
res.place(x = 430,y = 650)

root.mainloop()