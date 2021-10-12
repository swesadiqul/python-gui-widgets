from tkinter import*

root = Tk()
root.title("Python GUI Programming")
root.geometry("700x700")

FN = StringVar()
LN = StringVar()
DOB = StringVar()
i = IntVar()

def exit_call():
    exit()


# Create Menu & Menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File")
filemenu.add_command(label="Open")
filemenu.add_command(label="Open Module")
filemenu.add_command(label="Recent File")
filemenu.add_command(label="Module Browser")
filemenu.add_command(label="Path Browser")
filemenu.add_separator()
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Save as copy...")
filemenu.add_separator()
filemenu.add_command(label="Print Window")
filemenu.add_separator()
filemenu.add_command(label="Close")
filemenu.add_command(label="Exit", command=exit_call)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Select All")
editmenu.add_separator()
editmenu.add_command(label="Find")
editmenu.add_command(label="Find Again")
editmenu.add_command(label="Find Selection")
editmenu.add_command(label="Find in Files")
editmenu.add_command(label="Replace")
editmenu.add_command(label="Go to Line")
editmenu.add_command(label="Show Completions")
editmenu.add_command(label="Expand Word")
editmenu.add_command(label="Show Call Tip")
editmenu.add_command(label="Show Surrounding Parens")
menubar.add_cascade(label="Edit", menu=editmenu)

formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_command(label="Indent Region")
formatmenu.add_command(label="Dedent Region")
formatmenu.add_command(label="Comment Out Region")
formatmenu.add_command(label="Uncomment Region")
formatmenu.add_command(label="Tabify Region")
formatmenu.add_command(label="Untabify Region")
formatmenu.add_command(label="Toggle Tabs")
formatmenu.add_command(label="New Indent Width")
formatmenu.add_command(label="Format Paragraph")
formatmenu.add_command(label="Strip Trailind Whitespace")
menubar.add_cascade(label="Format", menu=formatmenu)

runmenu = Menu(menubar, tearoff=0)
runmenu.add_command(label="Python Shell")
runmenu.add_command(label="Check Module")
runmenu.add_command(label="Run Module")
runmenu.add_command(label="Run...Customized")
menubar.add_cascade(label="Run", menu=runmenu)

optionsmenu = Menu(menubar, tearoff=0)
optionsmenu.add_command(label="Configure IDLE")
optionsmenu.add_separator()
optionsmenu.add_command(label="Show Code Context")
optionsmenu.add_command(label="Zoom Height")
menubar.add_cascade(label="Options", menu=optionsmenu)

windowmenu = Menu(menubar, tearoff=0)
windowmenu.add_command(label="G:\SADIQUL ISLAM\PROGRAMMING\P_PROGRAM\Python GUI")
menubar.add_cascade(label="Window", menu=windowmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About IDLE")
helpmenu.add_separator()
helpmenu.add_command(label="IDLE Help")
helpmenu.add_command(label="Python Docs")
helpmenu.add_command(label="Turtle Demo")
menubar.add_cascade(label="Help", menu=helpmenu)

# Create Label and Entry

lbl = Label(root, text="Registration From", bg="gray", fg="white", relief="solid", width=30, font=("arial", 14,"bold"))
lbl.place(x=200,y=50)


lbl2 = Label(root, text="First Name",  font=("arial", 14,"bold"))
ey = Entry(root, textvar=FN)
lbl2.place(x=200,y=100)
ey.place(x=400, y=105)

lbl3 = Label(root, text="Last Name", font=("arial", 14,"bold"))
ey1 = Entry(root, textvar=LN)
lbl3.place(x=200,y=150)
ey1.place(x=400, y=155)

lbl4 = Label(root, text="Date Of Birth", font=("arial", 14,"bold"))
lbl4.place(x=200,y=200)
ey2 = Entry(root, textvar=DOB)
ey2.place(x=400, y=205)


lbl5 = Label(root, text="Country", font=("arial", 14,"bold"))
lbl5.place(x=200,y=250)

# Create ComBox
var = StringVar()

list1 = ["None", "Bangladesh", "India", "Butan","Srilanka","China"]

dt = OptionMenu(root,var,*list1)
var.set("Select Country")
dt.config(width=15)
dt.place(x=400, y=255)


lbl6 = Label(root, text="Pro.Language", font=("arial", 14,"bold"))
lbl6.place(x=200,y=300)

cb = Checkbutton(root, text="Python",  font=("arial",10,"bold"))
cb1 = Checkbutton(root, text="Java", font=("arial",10,"bold"))
cb2 = Checkbutton(root, text="C#",  font=("arial",10,"bold"))
cb.place(x=400, y=305)
cb1.place(x=460, y=305)
cb2.place(x=520, y=305)


lbl7 = Label(root, text="Gender", font=("arial", 14,"bold"))
lbl7.place(x=200,y=350)

rb = Radiobutton(root, text="Male", value=1, variable=i, font=("arial",10,"bold"))
rb1 = Radiobutton(root, text="Female", value=2, variable=i,  font=("arial",10,"bold"))
rb.place(x=400,y=355)
rb1.place(x=460,y=355)


root.config(menu=menubar)
root.mainloop()
