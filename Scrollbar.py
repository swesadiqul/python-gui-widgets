from tkinter import*





root = Tk()
root.title("Scrollbar")



frame = Frame(root)
frame.pack()

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, yscrollcommand= scroll.set)
for i in range(1,101):
    listbox.insert(END,"List " + str(i))
listbox.pack(side=LEFT)





scroll.config(command=listbox.yview)
root.geometry("700x700")
root.mainloop()
