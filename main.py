import pandas as pd 
from tkinter import *
from tkinter import ttk
from database import database
from plotting import plot_driver_comparison
from driver import driver
f1database = database()
output = f1database.getDrivers().sort_values(by="driverRef").driverRef.tolist()

display = Tk()
display.geometry("200x200")

l = Label(display,text = "F1 drivers speed comparison")

def show():
  #cb.get() retrieves selected driver
  lbl.config(text=cb.get())
  lbl2.config(text=cb2.get())
  driver1 = driver(cb.get(),f1database)
  driver2 = driver(cb2.get(),f1database)
  print(driver1,driver2)
  driver1_times = pd.merge(f1database.getLaptimes(),driver1.getDriverRecord(),on="driverId").query("raceId==841")[['time','lap']]
  driver2_times = pd.merge(f1database.getLaptimes(),driver2.getDriverRecord(), on="driverId").query("raceId==841")[['time','lap']]
  plot_driver_comparison(driver1_times['lap'].tolist(),driver2_times['lap'].tolist(),driver1_times['time'].tolist(),driver2_times['time'].tolist())

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

