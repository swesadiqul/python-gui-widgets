from tkinter import*

root = Tk()
root.geometry("600x600")
root.title("ComboBox")


label = Label(root, text="Country :", font=("arial",12,"bold"))
label.place(x=200,y=200)

var = StringVar()
list1 = "None","Bangladesh","India","Butan","Nepal","China"
droplist = OptionMenu(root, var, *list1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=300,y=200)






root.mainloop()
