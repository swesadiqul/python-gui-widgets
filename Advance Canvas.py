from tkinter import*


sadiq = Tk()
sadiq.title("Advance Canvas")
sadiq.geometry("600x600")


canvas = Canvas(sadiq, height=400, width=400, bg="blue")
canvas.place(x=100,y=50)
canvas.create_rectangle(100,100,300,300, fill="yellow",outline="yellow")
canvas.create_rectangle(150,150,250,250, fill="red", outline="red")

sadiq.mainloop()
