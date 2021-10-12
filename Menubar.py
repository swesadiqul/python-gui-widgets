from tkinter import*


def exit_call():
    exit()


root = Tk()
root.title("CREATE MENUBAR BY SADIQUL")
frame = Frame(root, width=700, height=700)

menubar = Menu(root, bg="gray")
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as.....")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit_call)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="paste")
editmenu.add_command(label="Select All")
editmenu.add_separator()
editmenu.add_command(label="Find")
menubar.add_cascade(label="Edit", menu=editmenu)

formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_command(label="Indent Region")
formatmenu.add_command(label="Dedent Region")
formatmenu.add_command(label="Comment Out Region")
formatmenu.add_command(label="Uncomment Region")
formatmenu.add_command(label="Tabify Region")
formatmenu.add_command(label="Untabify Region")
menubar.add_cascade(label="Format", menu=formatmenu)

runmenu = Menu(menubar, tearoff=0)
runmenu.add_command(label="Python Shell")
runmenu.add_command(label="Check Module")
runmenu.add_command(label="Run Module")
runmenu.add_command(label="Run Customized")
menubar.add_cascade(label="Run", menu=runmenu)

optionsmenu = Menu(menubar, tearoff=0)
optionsmenu.add_command(label="Configure IDLE")
optionsmenu.add_separator()
optionsmenu.add_command(label="Show code context")
optionsmenu.add_command(label="Zoom height")
menubar.add_cascade(label="Options", menu=optionsmenu)

root.config(menu=menubar)
frame.pack()
root.mainloop()
