from tkinter import *
import random
import webbrowser as wb

def log():
	wb.open("login.py")
def sign():
	wb.open("Signin.py")
arr = ["'We don't want to push our ideas on to customers, we simply want to make what they want.'", "'When you assume negative intent, you're angry.If you take away that anger and assume positive \n intent, you will  be amazed. '","'A brand for a company is like a reputation for a person. You earn reputation by trying to do \n hard things well.'"]
root = Tk()

root.config(bg = "#FFE0BE")
root.minsize(900 , 700)
root.maxsize(900,700)
#Background

img = PhotoImage(file = "bank.png")

photo = Label(image = img, width = 900 , height = 300)
photo.pack()

#frame
f1 = Frame(root, bg="#00ff00", borderwidth=1, relief = SUNKEN)

#To bring frame inside the main window which is root
#relief is to specif the design of the border

f1.place(x = 0 , y = 0)

l_1 =Label(f1, text = "    HOME          ABOUT US          CONTACT US       TERMS & POLICY                                                                                                                  ", font = "arial 13 bold" ,  bg = "#A9F1FF")
l_1.pack()

l = Label(text = "Welcome To Birla Bank" , font = "arial 25 bold ", fg = "orange" )
l.place(x = 300 , y = 30)

img1 = PhotoImage(file = "logo.png")

photo1 = Label(image = img1, width = 200 , height = 130 )
photo1.place(x = 300,  y = 310)

Label(text = "Quote Of A Day :-" ,  font = "comicssanms 16 bold underline italic"  , bg = "#FFE0BE").place(x = 20 , y = 470)
text = Label(text = str(random.choice(arr)) , fg = "red", font = "comicssanms 14 bold", bg = "#FFE0BE")
text.place(x = 5 , y = 520)



signin = Button(text = "SIGN IN", bg = "#7DD0CC", width = 25 , height = 2 ,font = "arial 12 bold", command = sign )
login = Button(text = "LOG IN", bg = "#7DD0CC", width = 25 , height = 2 , font = "arial 12 bold", command = log)

signin.place(x = 180, y = 600)
login.place(x = 480 , y = 600)
 




root.mainloop()