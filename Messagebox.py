from tkinter import*
from tkinter import messagebox

# showinfo,showerror,showwarning,

def info_sign():
    messagebox.showinfo("Message", "Do you know this symbol is name?")

def warning_sign():
    messagebox.showwarning("Python shell", "You are not young.please try aging!")

def error_sign():
    messagebox.showerror("Error", "Do you know this symbol is name?")

def exit_call():
    exit()

root = Tk()
root.title("PYTHON GUI WINDOW")


b1 = Button(root, text="Information", command=info_sign)
b1.pack()

b2 = Button(root, text="Warning", command=warning_sign)
b2.pack()

b3 = Button(root, text="Error", command=error_sign)
b3.pack()

b4 = Button(root, text="Exit", command=exit_call)
b4.pack()



root.geometry("400x400+120+120")
root.mainloop()
