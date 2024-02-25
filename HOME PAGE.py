from tkinter import *
import webbrowser as wb
import pandas as pd
import csv
from _csv import reader
import tkinter.messagebox as ms
from csv import writer

def loan():
    net = lst[2] + lst[2]*3
    ms.showinfo("Notification",f"Okay At Max You Can Take Loan of'{net}'")
    mon = int(input("Enter The Amount You Want To Take Loan"))
    while mon >= net:
        print("You Can't take This much Loan")
        mon = int(input("Enter The Amount You Want To Take Loan"))
    schemes = """ 1) Emi payment- 1 year
                                    interest rate = 5%(amount taken loan)
                                    each month - amount taken loan//12 + interest rate
                                2) Emi payment-2 year
                                    interest rate = 10%(amount taken loan)
                                    each month - amount taken loan//24 + interest rate"""
    print(schemes)
    c = int(input("Enter The Scheme No."))
    if c == 1:
        I_r = 5/100*mon
        ms.showinfo("NOTIFICATION",f"Okay You Have Pay Each Month'{mon// 12 + I_r}'")
        lst[3] = mon + lst[3]
        c4.delete(0,END)
        c4.insert(END , lst[3])
        d = pd.read_csv("array.csv")
        d["LOAN"][int(lst[1][5])] =  lst[3]
        d.to_csv("array.csv", index = False)
    else:
        I_r = 10/100*mon
        ms.showinfo("NOTIFICATION",f"Okay You Have Pay Each Month'{mon// 10 + I_r}'")
        lst[3] = mon + lst[3]
        c4.delete(0,END)
        c4.insert(END , lst[3])
        d = pd.read_csv("array.csv")
        d["LOAN"][int(lst[1][5])] =  lst[3]
        d.to_csv("array.csv", index = False)

    f = open("det.txt","w")
    info = lst[0] + " " +  lst[1] + " " + str(lst[2]) + " " + str(lst[3]) + " "
    f.write(info)
    f.close()
    
    

def transfer():
    global lst
    flag = False
    n = input("To Whom You Want to Transfer Money")
    j = 0
    
    while j < len(l):
        if n == l[j][1]:
            flag = True
            amt = int(input("Enter The amount you want to transfer"))
            lst[2] = lst[2] - amt
            bal = int(l[j][3]) + amt
            ms.showinfo("NOTification",f"Money Is Transfered Successfully to'{n}'",)
            c3.delete(0,END)
            c3.insert(END, lst[2])
            d = pd.read_csv("array.csv")
            d["BALANCE"][j - 1] = bal
            d["BALANCE"][int(lst[1][5])] = lst[2]
            d.to_csv("array.csv", index = False)
            f = open("det.txt","w")
            info = lst[0] + " " +  lst[1] + " " + str(lst[2]) + " " + str(lst[3]) + " "
            f.write(info)
            f.close()
            break
        j = j + 1
    if flag == False:
        ms.showinfo("WARNING", "Person Not Found")



def deposit():
    don = int(input("Okay How Much Amount You Want to add to your account"))
    lst[2] =  int(lst[2]) + don
    ms.showinfo("NOTIFICATION","We have Added The Balance in Your Account")
    c3.delete(0,END)
    c3.insert(END , lst[2])
    f = pd.read_csv("array.csv")
    f["BALANCE"][int(lst[1][5])] = lst[2]
    f.to_csv("array.csv",index = False)

    f = open("det.txt","w")
    info = lst[0] + " " +  lst[1] + " " + str(lst[2]) + " " + str(lst[3]) + " "
    f.write(info)
    f.close()
    

def Signout():
    k = ms.askquestion("Exit", "Are You sure to quit the application ?")
    if k == "yes":
        root.quit()
    


root = Tk()

root.config(bg = "#FFE0BE")
root.minsize(900 , 700)
root.maxsize(950, 750)

#Background

img = PhotoImage(file = "bank.png")

photo = Label(image = img, width = 900 , height = 250)
photo.pack(fill = "x")


f1 = Frame(root, bg="#00ff00", borderwidth=1, relief = SUNKEN)


f1.place(x = 0 , y = 0)

l_1 =Label(f1, text = "    HOME          ABOUT US          CONTACT US       TERMS & POLICY                                                                                                                  ", font = "arial 13 bold" ,  bg = "#A9F1FF")
l_1.pack()

Label(text = "SCHEMES" , fg = "red" , font = " comicsanms 20 bold italic underline" , bg = "#FFE0BE").place(x = 20 , y = 260)

Label(text = "1. In this Bank Loan Amount cannot exceed  50 Million (Rs. 5000000)",font = " comicsanms 14 bold " , bg = "#FFE0BE").place(x = 20 , y = 300)
Label(text = "2. Interest Rate is 7 % Anually and Quaterly 5%", font = " comicsanms 14 bold " , bg = "#FFE0BE").place(x = 20 , y = 330) 
Label(text = "3. This Bank Does not Accepts EMIs " , font = " comicsanms 14 bold " , bg = "#FFE0BE").place(x = 20 , y = 360)
Label(text = "4. Loan can Be taken for any Purpose ", font = " comicsanms 14 bold " , bg = "#FFE0BE").place(x = 20 , y = 390)

Label(text = "USER DETAILS" , fg = "red" , font = " comicsanms 18 bold italic underline" , bg = "#FFE0BE").place(x = 20 , y = 430)


img1 = PhotoImage(file = "logo.png")

photo1 = Label(image = img1 , bg = "#FFE0BE")
photo1.place(x = 20 , y = 470)

r1 = Entry(root ,font = " comicsanms 14 bold ")
r2 = Entry(root, font = " comicsanms 14 bold ")
r3 = Entry(root, font = " comicsanms 14 bold ")
r4 = Entry(root, font = " comicsanms 14 bold ")

r1.place(x = 160 , y = 470)
r2.place(x = 160 , y = 495)
r3.place(x = 160 , y = 520)
r4.place(x = 160 , y = 545)

c1 = Entry(root, font = " comicsanms 14 bold ")
c2 = Entry(root, font = " comicsanms 14 bold ")
c3 = Entry(root, font = " comicsanms 14 bold ")
c4 = Entry(root, font = " comicsanms 14 bold ")

c1.place(x = 380 , y = 470)
c2.place(x = 380 , y = 495)
c3.place(x = 380 , y = 520)
c4.place(x = 380 , y = 545)

r1.insert(END, "NAME")
r2.insert(END, "ACCOUNT NO.")
r3.insert(END, "BALANCE")
r4.insert(END, "LOAN TAKEN")

Label(text = "*   (Click One of The Buttons to perform The task Which You Want ) * ", fg = "black" , font = " comicsanms 11 italic " , bg = "#FFE0BE").place(x = 20 , y = 575 )

loan = Button(text = "LOAN" , bg = "#A9F1FF" , height = 2, width = 15 , font = "arial 11 bold" , command = loan)
deposit = Button(text = "DEPOSIT" , bg = "#A9F1FF", height = 2, width = 15 , font = "arial 11 bold", command = deposit)
transfer = Button(text = "TRANSFER", bg = "#A9F1FF", height = 2 , width = 15 , font = "arial 11 bold" , command = transfer)
signout = Button(text = "Sign Out", bg = "#00ff00", height = 1 , width = 10 , font = "arial 11 bold" , command = Signout)

signout.place(x = 850 , y = -5)
loan.place(x = 150 , y = 605)
deposit.place(x = 320 , y = 605)
transfer.place(x = 500 , y = 605)
 

f = open("det.txt","r")
st = f.read()
i = 0
s = ""
lst = []
count = 0
while i < len(st):
    if st[i] == " ":
        i = i + 1
        count = count + 1
        if count <=2:
            lst.append(s)

        else:
            lst.append(int(s))

        s = ""
    if i < len(st):
        s = s + st[i]
    i = i + 1
f.close()

c1.insert(END , lst[0])
c2.insert(END , lst[1])
c3.insert(END , lst[2])
c4.insert(END , lst[3])





file = open("array.csv", "r")
csv_reader = csv. reader(file)

l = []

for row in csv_reader:
    if row != []:
     l.append(row)



root.mainloop()
