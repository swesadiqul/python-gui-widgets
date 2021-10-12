from tkinter import*



root = Tk()
root.title("Text box")

# Syntax: text = Text ( root, option, ... )
# Options: width,height,wrap,padx,pady,bd,relief,selectbackground


text = Text(root, width=60, height=30, wrap=WORD, padx=10, pady=10, bd=5, relief="groove", selectbackground="orange")
text.place(x=100, y=50)





root.geometry("700x700")
root.mainloop()
