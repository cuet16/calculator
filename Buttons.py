from tkinter import *

root = Tk()

def myClick():
    myLabel = Label (root, text = "Look I clicked a button!")
    myLabel.pack()

myButton = Button(root, text =  "Click me!", padx = 50, command=myClick ) #creates button, padx = for the width pady for the height, command is calling the function that defined and assigning it to the button.
# for the MyClick function remember not to put brackets at the end as done with most functions in python.

myButton.pack() #locates it on the window

root.mainloop()