from tkinter import*



root = Tk() # Class in this program
root.title("Button") # Title in this program

# Create button function
def result_view():
    print("Welcome to graphical user interface programming!")

# Create button1
b1  = Button(root, text="Result", bg="lightgreen", bd=10, fg="black", activebackground="lightgreen", activeforeground="blue", highlightcolor="blue",
             justify="left",relief="groove", font=("arial",12,"bold","underline","italic"),command=result_view)

# Create button2
b2  = Button(root, text="Exit", bg="lightgreen", bd=10, fg="black", activebackground="lightgreen", activeforeground="blue", highlightcolor="blue",
             justify="left",relief="groove", font=("arial",12,"bold","underline","italic"),command=quit)


# Close button1
b1.place(x=300, y=50)
# Close button2
b2.place(x=350, y=100)




root.geometry("700x700") # Window size
root.mainloop() # End of the GUI program
