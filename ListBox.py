from tkinter import*



root = Tk()
root.geometry("700x700")
root.title("ListBox")

# Listbox syntax: Lb1 = Listbox ( root, option, ... )
#master − This represents the parent window.
"""###options − Here is the list of most commonly used options for this widget.
        These options can be used as key-value pairs separated by commas."""

# Options are: bg,bd,cursor,font,fg,height,highlightcolor,highlightthickness,relief,selectbackground,

Lb1 = Listbox(root, width=20,height=15)
Lb1.insert(1, "Python")
Lb1.insert(2, "Java")
Lb1.insert(3, "PHP")
Lb1.insert(4, "C#")
Lb1.insert(5, "C")
Lb1.insert(6, "C++")
Lb1.insert(7, "Perl")
Lb1.insert(8, "Java script")
Lb1.insert(9, "Fortrain")
Lb1.pack()

root.mainloop()
