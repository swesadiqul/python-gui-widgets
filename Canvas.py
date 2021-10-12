from tkinter import *

master = Tk()
master.geometry("600x600")
master.title("Canvas")

canvas = Canvas(master, width=200, height=200, bg="blue") 
canvas.grid(padx=200,pady=50) 


master.mainloop() 
