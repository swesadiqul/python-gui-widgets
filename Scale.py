from tkinter import*



root = Tk()
root.title("Scale")
root.geometry("700x700")

label = Label(root, text="")


s = Scale(root, from_=0, to=100, orient=VERTICAL, width=20, sliderlength=20,length=200,highlightbackground="green", bd=10, relief="solid")
s.pack()




root.mainloop()
