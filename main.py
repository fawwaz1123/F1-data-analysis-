import pandas as pd 
from tkinter import *
from tkinter import ttk
from database import database
from plotting import plot_driver_comparison
database = database()
output = database.getDrivers().sort_values(by="driverRef").driverRef.tolist()

display = Tk()
display.geometry("200x200")

l = Label(display,text = "F1 drivers speed comparison")

def show():
  #cb.get() retrieves selected driver
  lbl.config(text=cb.get())
  lbl2.config(text=cb2.get())
  driver1 = cb.get()
  driver2 = cb2.get()
  print(driver1,driver2)
  plot_driver_comparison(database.getLaptimes())

#combobox1
cb =ttk.Combobox(display, values=output)
cb.set("select a driver")
cb.pack()

cb2 =ttk.Combobox(display, values=output)
cb2.set("select a driver")
cb2.pack()


#display button for selection
Button(display,text="Show selection and compare", command=show).pack()

#label to show selected driver
lbl = Label(display, text="")
lbl.pack()
lbl2 = Label(display, text="")
lbl2.pack()

#mainloop ensures gui is constantly running
display.mainloop()

