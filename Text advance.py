from tkinter import*



root = Tk()
root.title("Text box advance")

def print_me():
    select1 = text.selection_get()
    print(select1)
    result = text.get(1.0, END) # Method options: get(), selection_get()
    pos = text.search(result, 1.0, stopindex=END)
    print(pos)
    print(result)

def clear_me():
    text.delete(1.0, END)


text = Text(root, width=60, height=30, padx=5, pady=5, wrap=WORD, bd=3, relief="groove", selectbackground="gray")
text.insert(INSERT, "Hello guys, I am Sadiqul Islam....")
text.place(x=100, y=50)


b1 = Button(root, text="Clic here", bg="gray", command=print_me)
b1.place(x=325, y=550)

b2 = Button(root, text="Remove Text", bg="gray", command=clear_me)
b2.place(x=325, y=600)


root.geometry("700x700")
root.mainloop()
