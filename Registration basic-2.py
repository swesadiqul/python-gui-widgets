from tkinter import*



wn = Tk()
wn.title("Registration From")
wn.geometry("700x700")


fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()

def print_call():
    first=fn.get()
    sec=ln.get()
    dob1=dob.get()
    var1=var.get()
    print(f"Your Full Name is: {first}{sec}")
    print(f"You Age is: {dob1}")
    print(f"Your Country is: {var1}")


def exit_call():
    exit()


label_0 = Label(wn, text="Registration From", relief="solid", width=30, bg="gray", fg="white", font=("arial",15,"bold")).place(x=170,y=50)

label_1 = Label(wn, text="First Name :", fg="black", font=("arial",12,"bold")).place(x=200,y=150)
entry_1 = Entry(wn, textvar=fn, width=20,).place(x=350,y=155)

label_2 = Label(wn, text="Last Name :", fg="black", font=("arial",12,"bold")).place(x=200,y=200)
entry_2 = Entry(wn, textvar=ln).place(x=350,y=205)


label_3 = Label(wn, text="DOB            :", fg="black", font=("arial",12,"bold")).place(x=200,y=250)
entry_3 = Entry(wn, textvar=dob).place(x=350,y=255)


label_4 = Label(wn, text="Country     :", fg="black", font=("arial",12,"bold")).place(x=200,y=300)

var = StringVar()

list1 = ["Bangladesh","India","Nepal","Butan","Canada","Pakistan","China"]
droplist = OptionMenu(wn, var,*list1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=350,y=305)


button_0 = Button(wn, text="Sing Up", relief="solid", bg="green", fg="white", width=10, font=("arial",14,"bold"), command=print_call).place(x=200,y=500)
button_1 = Button(wn, text="Quit", relief="solid", bg="green", fg="white", width=10, font=("arial",14,"bold"), command=exit_call).place(x=400,y=500)

wn.mainloop()
