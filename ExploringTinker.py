from tkinter import *

root = Tk() ## happens before anything, this is the main window

myLabel1 = Label(root, text="Hello World!") ##creating a label widget, first we need to define, then locate it

myLabel2 = Label(root, text="My name is Cesar") ##creating a label widget, first we need to define, then locate it

myLabel3 = Label(root, text="       ") ##creating a label widget, first we need to define, then locate it

# myLabel.pack() # we are just locating the Label widget in the space that is available (shoving it into the screen)

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 5)
myLabel3.grid(row = 1, column = 1)

# we need to create a loop that tracks every movement in the GUI

root.mainloop()