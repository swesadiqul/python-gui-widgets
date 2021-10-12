from tkinter import*

def exit_page():
    exit()




root = Tk()
root.title("PanedWindow")

pw = PanedWindow(root, bg="green", width=300, height=200)
b = Button(pw, text="Close", bg="yellow", activebackground="yellow", font=("arial", 12, "bold"), command=exit_page)

pw.place(x=200, y=50)
b.place(x=120, y=10)






root.geometry("700x700")
root.mainloop()
