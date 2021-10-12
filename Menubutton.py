from tkinter import*




root = Tk()
root.title("Menubutton.")


mb = Menubutton(root, text="This is a menu", bg="gray",font=("arial",12,"bold"))
mb.menu = Menu(mb, tearoff=1)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1", command=lambda: print("This is option 1"))
mb.menu.add_command(label="Option 2", command=lambda: print("This is option 2"))
mb.place(x=200,y=50)





root.geometry("700x700")
root.mainloop()
