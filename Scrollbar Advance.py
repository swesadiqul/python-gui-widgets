from tkinter import*



window = Tk()
window.title("Listbox and Scrollbar")

frame = Frame(window)

ilist = Listbox(frame, height=18, width=20, font=("arial",20,"bold"), justify=CENTER, bg="cyan")
scroll = Scrollbar(frame, command=ilist.yview)


ilist.configure(yscrollcommand=scroll.set)
ilist.pack(side=LEFT)






scroll.pack(side=RIGHT, fill=Y)



for i in range(501):
    ilist.insert(END, i)



frame.pack()
window.mainloop()
