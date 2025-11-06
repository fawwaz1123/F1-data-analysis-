import pandas as pd 
from tkinter import *
from tkinter import ttk
from database import database
database = database()
output = database.getDrivers().sort_values(by="driverRef").driverRef.tolist()

display = Tk()
display.geometry("200x200")

l = Label(display,text = "F1 drivers speed comparison")

def show():
  #cb.get() retrieves selected driver
  lbl.config(text=cb.get())
  print(cb.get())

#combobox
cb =ttk.Combobox(display, values=output)
cb.set("select a driver")
cb.pack()

#display button for selection
Button(display,text="Show selection", command=show).pack()

#label to show selected driver
lbl = Label(display, text="")
lbl.pack()

#mainloop ensures gui is constantly running
display.mainloop()

