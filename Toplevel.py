from tkinter import*



def call_me():
    top = Toplevel()
    top.title("New window open")
    top.geometry("700x700")
    b1 = Button(top, text="Close", bg="gray", fg="white", command=lambda: print(exit()))
    b1.place(x=300, y=50)



root = Tk()
root.title("Toplevel")


b = Button(root, text="Click here!", bg="purple", fg="white", command=call_me)
b.place(x=300, y=50)





root.geometry("700x700")
root.mainloop()
