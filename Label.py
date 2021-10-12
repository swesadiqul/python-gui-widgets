# Python GUI programm
# By@Sadiqul Islam
# Part-1[Label]


from tkinter import*

window = Tk()
window.geometry("600x600")
window.title("Create Label")




lb1 = Label(window, text="Registration From", relief="solid", width=20, bg="gray", fg="white", font=("Times",18,"bold", "italic", "underline"))
lb1.place(x=150,y=50)

lb2 = Label(window, text="First Name", font=("arial 12 bold"))
lb2.place(x=150,y=100)

lb3 = Label(window, text="Last Name", font=("arial",12,"bold"))
lb3.place(x=150,y=150)

lb4 = Label(window, text="Date Of Birth", font=("arial",12,"bold"))
lb4.place(x=150,y=200)

window.configure(background="blue")
window.mainloop()
