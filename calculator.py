from tkinter import *

root = Tk()
root.title("Calculator")

_entry = Entry(root, width = 50, borderwidth = 5)
_entry.grid(row = 0, column = 0, columnspan = 3) #column will span over other columns

def button_add():
    return

def myClick():
    myLabel = Label (root, text = "Look I clicked a button!")
    myLabel.pack()

def button_click(number):
    #_entry.delete(0, END) #deletes what is already in the box, however this is a problem if you want to enter more than 1 digit numbers
    current = _entry.get() #gets the number from the button and stores it in variable "current"
    _entry.delete(0,END) #then it clears the screen
    _entry.insert(0, str(current) + str(number)) # then it inserts the current number plus the nuew number from the next button pressed
    #                                            #we also make these strings

    
# Define buttons
Button_0 = Button(root, text =  "0", padx = 40, command=lambda: button_click(0)) #lambda passes the number to he button
Button_1 = Button(root, text =  "1", padx = 40, command=lambda: button_click(1)) 
Button_2 = Button(root, text =  "2", padx = 40, command=lambda: button_click(2))
Button_3 = Button(root, text =  "3", padx = 40, command=lambda: button_click(3))
Button_4 = Button(root, text =  "4", padx = 40, command=lambda: button_click(4))
Button_5 = Button(root, text =  "5", padx = 40, command=lambda: button_click(5))
Button_6 = Button(root, text =  "6", padx = 40, command=lambda: button_click(6))
Button_7 = Button(root, text =  "7", padx = 40, command=lambda: button_click(7))
Button_8 = Button(root, text =  "8", padx = 40, command=lambda: button_click(8))
Button_9 = Button(root, text =  "9", padx = 40, command=lambda: button_click(9))
Button_equal = Button(root, text =  "=", padx = 40, command=lambda: button_click())
Button_clear = Button(root, text =  "C", padx = 40, command=lambda: button_click())
Button_sum = Button(root, text =  "+", padx = 40, command=lambda: button_click())


#Put buttons on the screen (grid)
Button_0.grid(row = 5, column = 1)
Button_1.grid(row = 4, column = 0)
Button_2.grid(row = 4, column = 1)
Button_3.grid(row = 4, column = 2)
Button_4.grid(row = 3, column = 0)
Button_5.grid(row = 3, column = 1)
Button_6.grid(row = 3, column = 2)
Button_7.grid(row = 2, column = 0)
Button_8.grid(row = 2, column = 1)
Button_9.grid(row = 2, column = 2)
Button_equal.grid(row = 5, column = 3, columnspan = 1, sticky = W+E)
Button_clear.grid(row = 1, column = 3, columnspan = 1, sticky = W+E)
Button_sum.grid(row = 4, column = 3, columnspan = 1, sticky = W+E)


root.mainloop()