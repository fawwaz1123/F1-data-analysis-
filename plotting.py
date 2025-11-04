import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

laptimes= pd.read_csv('lap_times.csv')
drivers = pd.read_csv('drivers.csv')
times = laptimes.query('raceId == 841')[['lap','time']]
driverLap_times = pd.merge(drivers,laptimes,how = 'inner', on= 'driverId')
hamilton_times = driverLap_times.query("(driverRef == 'hamilton') and (raceId == 841)")

print(times)
print(laptimes.columns)
print(driverLap_times)
print(hamilton_times)


hamilton_times[['lap','time']].plot(x='time',y='lap')
plt.show()