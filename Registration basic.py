from tkinter import*

wn = Tk()
wn.geometry("500x500")
wn.title("Registration From")

def printt():
    print("Demo tkinter")

def exit1():
    exit()

label1 = Label(wn, text = "Registration From", relief = "solid", width=20, font = ("arial",19,"bold"))
label1.place(x=90,y=53)

label2 = Label(wn, text = "First Name :", width=20, font = ("arial",12,"bold"))
label2.place(x=80,y=130)

label3 = Label(wn, text = "Last Name :", width=20, font = ("arial",12,"bold"))
label3.place(x=80,y=160)

button1 = Button(wn, text = "Login", width=12, bg="brown",fg="white", command=printt)
button1.place(x=150,y=380)

button2 = Button(wn, text = "Exit", width=12, bg="brown",fg="white", command=exit1)
button2.place(x=280,y=380)

wn.mainloop()
