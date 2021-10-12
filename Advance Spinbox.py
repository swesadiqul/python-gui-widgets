from tkinter import*


def exit_value():
    result = sb.get()
    print(result)


wn = Tk()
wn.title("Advance Spinbox-1")
wn.geometry("700x700")


l1 = Label(wn, text="Spinbox1", bg="gray", relief="solid", width=10, font=("Arial",12,"bold"))
l1.place(x=260,y=50)
sb = Spinbox(font=("Verdana",12,"bold"), from_=0, to=15, width=10)
sb.place(x=250,y=100)

b = Button(wn, text="Execution", bg="purple", fg="white", font=("arial", 10, "bold"), command=exit_value)
b.place(x=270, y=150)



wn.mainloop()




