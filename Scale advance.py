from tkinter import *

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
scale = Scale( root, variable = var, orient=HORIZONTAL,  bg="green", activebackground="orange", highlightcolor="blue", fg="yellow" )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel, anchor=CENTER)
button.place(x=300,y=200)

label = Label(root)
label.pack()

root.geometry("700x700")
root.mainloop()
