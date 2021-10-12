from tkinter import*



root = Tk()
root.geometry("700x700")
root.title("ListBox-2")


#selectmode

"""Determines how many items can be selected, and how mouse drags affect the selection −
#BROWSE − Normally, you can only select one line out of a listbox.
    If you click on an item and then drag to a different line, the selection will follow the mouse. This is the default.
#SINGLE − You can only select one line, and you can't drag the mouse.wherever you click button 1, that line is selected.
#MULTIPLE − You can select any number of lines at once. Clicking on any line toggles whether or not it is selected.
#EXTENDED − You can select any adjacent group of lines at once by clicking on the first line and dragging to the last line."""



Lb1 = Listbox(root, width=20,height=15, selectmode=BROWSE)
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
