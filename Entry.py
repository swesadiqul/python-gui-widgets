from tkinter import*

window = Tk()
window.geometry("600x600")
window.title("Create Entry")

var_01 = StringVar()
var_02 = StringVar()
var_03 = StringVar()
var_04 = StringVar()


entry_01 = Entry(window, textvar=var_01)
entry_01.place(x=300,y=105)

entry_02 = Entry(window, textvar=var_02)
entry_02.place(x=300,y=155)

entry_03 = Entry(window, textvar=var_03)
entry_03.place(x=300,y=205)


window.mainloop()
