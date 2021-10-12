from tkinter import*


def text_print():
    entry = ent.get()
    rd_ck = rd_v.get()
    text = txt.get(1.0, END)
    print(entry)
    print(rd_ck)
    print(text)



root = Tk()
root.title("Text advance-1")

l1 = Label(root, text="Name:")
l2 = Label(root, text="Gender:")
l3 = Label(root, text="Discription:")

ent = Entry(root)

rd_v = IntVar()

rd1 = Radiobutton(root, text="Male", variable=rd_v, value=1)
rd2 = Radiobutton(root, text="Female", variable=rd_v, value=2)




txt = Text(root, width=30, height=10, wrap=WORD)
b = Button(root, text="REGISTER", bg="purple", fg="white", command=text_print)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)

ent.grid(row=0, column=1)

rd1.grid(row=1, column=1)
rd2.grid(row=1, column=2)

b.grid(row=10, column=1)
txt.grid(row=3, column=1)



root.geometry("700x700")
root.mainloop()
