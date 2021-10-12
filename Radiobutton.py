from tkinter import*


root = Tk()
root.title("Radiobutoon")

v = IntVar()

radioButton1 = Radiobutton(root, text="Python",value=0,variable=v, command=lambda: print(v.get()))
radioButton2 = Radiobutton(root, text="Java",value=1, variable=v, command=lambda: print(v.get()))

radioButton1.pack()
radioButton2.pack()


root.geometry("700x700")
root.mainloop()
