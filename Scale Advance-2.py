from tkinter import*




top = Tk()
top.geometry("700x700")
top.title("First gui program.")


label = Label(top, text="")
label.pack()

def show(val):
    label.configure(text=val)

scale = Scale(top, from_=0, to=100, orient=HORIZONTAL, length=500, width=20, tickinterval=5, command=show)
scale.pack()




top.mainloop()
