from tkinter import*
from tkinter import messagebox


# Messagebox syntax : tkMessageBox.FunctionName(title, message [, options])
# This is the name of the appropriate message box function.
#showinfo()
#showwarning()
#showerror ()
#askquestion()
#askokcancel()
#askyesno ()
#askretrycancel ()

#title − This is the text to be displayed in the title bar of a message box.

#message − This is the text to be displayed as a message.

"""options − options are alternative choices that you may use to tailor a standard message box.
Some of the options that you can use are default and parent.
The default option is used to specify the default button, such as ABORT, RETRY, or IGNORE in the message box.
The parent option is used to specify the window on top of which the message box is to be displayed."""

def call_me():
    answer = messagebox.askquestion("Exit","Do you really want to exit?")
    if answer=="yes":
        print("Good job.")
    else:
        print("What's the wrong with you? why don't you eat?")


root = Tk()
root.title("First GUI program")
root.geometry("300x300")

label_01 = Label(root, text= "Welcome to Tkinter", bg="yellow", fg="blue",relief= "solid", font=("arial", 12, "bold"))#.place(x=600,y=50)
#label_01.pack(fill=BOTH, pady=2, padx=2, expand= True)
label_01.pack()

# GROOVE,RIDGE,SUNKEN,RAISED(relief matarials)
button= Button(root, text= "Demo",bg="brown",fg="white", relief=GROOVE,font=("arial", 12, "bold"),command=call_me)
                                                  
button.place(x=110,y=110)
root.mainloop()
