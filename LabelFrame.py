from tkinter import*

def exit_value():
    value = entry.get()
    print(value)


root = Tk()
root.title("LabelFrame")

v = StringVar()


frame = LabelFrame(root, text="Input", padx=10, pady=10)
entry = Entry(frame, textvar=v)

frame.pack()
entry.pack()

b = Button(root, text="Execution", bg="purple", fg="white", activebackground="purple", command=exit_value)
b.pack()



root.geometry("700x700")
root.mainloop()
