from comparison import compare
from tkinter import *
from tkinter import ttk
from database import database

display = Tk()
display.geometry("200x200")

l = Label(display,text = "F1 data analysis")

def show():
  compare(database())

Button(display,text="Press to compare 2 drivers race data",command=show).pack()

display.mainloop()