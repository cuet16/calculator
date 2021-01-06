from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg = "cyan")
e.pack()
e.get()
e.insert(0, "enter your name: ") # this puts a default text inside the box

def myClick():
    myLabel = Label (root, text = "Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text =  "Enter your name", padx = 50, command=myClick ) #creates button, padx = for the width pady for the height, command is calling the function that defined and assigning it to the button.
# for the MyClick function remember not to put brackets at the end as done with most functions in python.

myButton.pack() #locates it on the window

root.mainloop()