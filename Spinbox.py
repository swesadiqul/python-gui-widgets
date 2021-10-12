from tkinter import*


root = Tk()


def print_call():
    print(spinbox2.get())

       
root.title("Spinbox")
root.geometry("700x700")

#ambiguous option "-pad": must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky


label_1 = Label(root, text="Spinbox-1:", bg="gray", fg="white", font=("arial",12,"bold"))
label_1.grid(padx=250,pady=50)

#1.Spinbox
spinbox1 = Spinbox(root, from_=0, to=10)
spinbox1.place(x=250, y=100)






label_2 = Label(root, text="Spinbox-2:", bg="gray", fg="white", font=("arial",12,"bold"))
label_2.place(x=250,y=180)

#2.Spinbox
spinbox2 = Spinbox(root, from_=0, to=31)
spinbox2.place(x=250, y=220)

button2 = Button(root, text="Value", bg="green", fg="white", relief="groove", font=("arial",12,"bold"),command=print_call)
button2.place(x=280, y=250)


root.mainloop()
