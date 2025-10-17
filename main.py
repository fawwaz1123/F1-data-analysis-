import pandas as pd 
from tkinter import *
from tkinter import ttk

data = pd.read_csv("F1Drivers_Dataset.csv")
output = data.Driver.tolist()

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

print(show())
