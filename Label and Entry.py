from tkinter import*

window = Tk()
window.geometry("600x600")
window.title("Python GUI Program")




var_01 = StringVar()
var_02 = StringVar()
var_03 = StringVar()
var_04 = StringVar()


label_01 = Label(window, text="Registration From", relief="solid", width=20, bg="gray", fg="white", font=("arial",18,"bold"))
label_01.place(x=150,y=50)

label_02 = Label(window, text="First Name", font=("arial",12,"bold"))
label_02.place(x=150,y=100)
entry_01 = Entry(window, textvar=var_01)
entry_01.place(x=300,y=105)

label_03 = Label(window, text="Last Name", font=("arial",12,"bold"))
label_03.place(x=150,y=150)
entry_02 = Entry(window, textvar=var_02)
entry_02.place(x=300,y=155)

label_04 = Label(window, text="Date Of Birth", font=("arial",12,"bold"))
label_04.place(x=150,y=200)
entry_03 = Entry(window, textvar=var_03)
entry_03.place(x=300,y=205)





label_05 = Label(window, text="Country", font=("arial",12,"bold"))
label_05.place(x=150,y=250)
entry_04 = Entry(window, textvar=var_04)
entry_04.place(x=300,y=255)

window.mainloop()
