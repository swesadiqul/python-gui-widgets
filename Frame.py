from tkinter import*

root = Tk()
root.title("Python GUI")

# Frame syntax: w = Frame ( master, option, ... )
# Frame(bg,bd,cursor,height,width,highlightbackground,highlightcolor,relief)

frame = Frame(root, width=300, height=300, bg="gray",highlightbackground="red", relief="flat" )
frame.pack()


root.mainloop()
