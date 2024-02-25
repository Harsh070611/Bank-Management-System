from tkinter import *
from _csv import reader
import pandas as pd
from csv import writer
import csv
import webbrowser as wb
import tkinter.messagebox as ms

def reset():
	u_name.delete(0,END)
	u_pass.delete(0,END)
	u_email.delete(0,END)
	u_balance.delete(0,END)
	u_dob.delete(0,END)

	wb.open("HOME PAGE.py")

#main processor for signing in

def submit():
	if u_name != "" or u_email != "" or u_pass != "" or u_balance != "" or  u_dob != "" :
			name_ = u_name.get()
			balance_ = u_balance.get()
			email_ = u_email.get()
			dob_ = u_dob.get()
			password_ =  u_pass.get()
		
			array = ["Name", "Password","Balance","Account No.","Loan Taken"]


			file = open("array.csv", "r")
			csv_reader = csv. reader(file)

			numberofpersons = []
			for row in csv_reader:
			  numberofpersons.append(row)

			file.close()

			j = len(numberofpersons)
			

			account = "birla" + str(j-1) 

			loann = 0
			
			df = pd.DataFrame([[name_, password_, balance_ , account, loann]], columns= array )

			file = open("array.csv", "r")
			csv_reader = csv. reader(file)

			l = []
			#Getting the info of data into a List

			for row in csv_reader:
			    if row != []:
			        l.append(row)


			flag = True
			file.close()

			i = 0
			# checking the existing username and password

			while i < len(l):
			    if name_ == str(l[i][1]) and str(password_) == str(l[i][2]):
			        flag = False
			        ms.showinfo("WARNING","Username and Password are Under use, Try with Another name and password")
			        break
			    i = i + 1

			if flag == True:  
			    with open("array.csv", 'a') as f:
			            df.to_csv(f, header=False)
			      
			    det = [j,name_,password_,balance_, account,loann]
			    l.append(det)

			    index_current = len(l) - 1
			    ms.showinfo("NOTIFICATION","You Are Successfully Registered Into The Birla Bank")
			    ms.showinfo("Account No.",f"Your Bank Account No  is  ' {account} ' ")
			    wb.open("HOME PAGE.py")

			f = open("det.txt","w")
			info = name_ + " " +  account + " " + str(balance_) + " " + str(loann) + " "
			f.write(info)
			f.close()

	else:
		ms.showinfo("WARNING!!","Please Fill Up All The Requirements" )

def details_user():
	name_ = u_name.get()
	balance_ = u_balance.get()
	password_ =  u_pass.get()
	account = "birla" + str(j - 1) 

#design part

root = Tk()
root.maxsize(1000 , 750)
root.minsize(900 , 700)

root.config(bg = "#FFE0BE")
img = PhotoImage(file = "bank.png")

photo = Label(image = img, width = 900 , height = 270)
photo.pack()

f1 = Frame(root, bg="#00ff00", borderwidth=1, relief = SUNKEN)


f1.place(x = 0 , y = 250)

l_1 =Label(f1, text = "                                                                                                                                                                                      ", font = "arial 13 bold" ,  bg = "#A9F1FF" , height = 2)
l_1.pack()

l = Label(text = "Welcome To Birla Bank" , font = "arial 25 bold")
l.place(x = 300 , y = 10)

img1 = PhotoImage(file = "logo.png")

photo1 = Label(image = img1, width = 200 , height = 130 )
photo1.place(x = 310,  y = 310)

name = Label(text = "Username", fg = "red" , font = "arial 11 bold")
password = Label(text = "Password",fg = "red" , font = "arial 11 bold")
email = Label(text = "Email Id",fg = "red",font = "arial 11 bold")
balance = Label(text = "BALANCE",fg = "red",font = "arial 11 bold")
dob = Label(text = "D.O.B (DD/MM/YYYY)", font = "arial 11 bold" , fg = "red")

Label(text = "USER DETAILS", font = "arial 15 bold", bg = "#FFE0BE").place( x = 320 , y = 450)

name.place(x = 100 , y = 500)
password.place(x = 100 , y = 550)
email.place(x = 100 , y = 600)
balance.place(x = 420 , y = 495)
dob.place(x = 400 , y = 545)
 
u_name = Entry(root)
u_pass = Entry(root)
u_email = Entry(root)
u_balance = Entry(root)
u_dob = Entry(root)

u_name.place(x = 210 , y = 500)
u_pass.place(x = 210 , y = 550)
u_email.place(x = 210 , y = 600)
u_balance.place(x = 560 , y = 495)
u_dob.place(x = 560 , y = 545)

ckbtn = Checkbutton(text = "I Accept All the Terms and Conditions" , font = "arial 12 bold", bg = "#FFE0BE")
ckbtn.place(x = 400 , y = 590)


sub = Button(text = "SUBMIT", bg = "#7DD0CC", width = 10 , height = 1 ,font = "arial 12 bold", command = submit)
res = Button(text = "RESET", bg = "#7DD0CC", width = 10 , height = 1 , font = "arial 12 bold", command = reset)
sub.place(x = 240,y = 650)
res.place(x = 430,y = 650)

img2 = PhotoImage(file = "line.png",width = 20)

photo = Label(image = img2)
photo.place(x = 370 , y = 480)

home = Button(text = "HOME", bg = "#A9F1FF",  height = 1 ,font = "arial 12 bold", command = submit)
contact = Button(text = "CONTACT US", bg = "#A9F1FF",  height = 1 ,font = "arial 12 bold", command = submit)
about = Button(text = "ABOUT US", bg = "#A9F1FF"  , height = 1 ,font = "arial 12 bold", command = submit)
terms = Button(text = "TERMS & Conditions", bg = "#A9F1FF", height = 1 ,font = "arial 12 bold", command = submit)


home.place(x = 10 , y = 256)
contact.place(x = 140 , y = 256)
about.place(x = 300 , y = 256)
terms.place(x = 450 , y = 256)

root.mainloop()
