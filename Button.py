from tkinter import*
from tkinter import messagebox



wn = Tk()
wn.title("Registration From")
wn.geometry("700x700")

def print_call():
    messagebox.showinfo("Welcome","Login successfully done!")
    

def exit_call():
    exit()




button_0 = Button(wn, text="Sing Up", relief="solid", bg="green", fg="white", width=10, font=("arial",14,"bold"), command=print_call)
button_0.place(x=200,y=500)
button_1 = Button(wn, text="Quit", relief="solid", bg="green", fg="white", width=10, font=("arial",14,"bold"), command=exit_call)
button_1.place(x=400,y=500)

wn.mainloop()
