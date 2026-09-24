import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from database import database

database = database()

times = database.getLaptimes().query('raceId == 841')[['lap','time']]
driverLap_times = pd.merge(database.getDrivers(),database.getLaptimes(),how = 'inner', on= 'driverId')
hamilton_times = driverLap_times.query("(driverRef == 'hamilton') and (raceId == 841)")

hamilton_times[['lap','time']].plot(x='time',y='lap')
plt.show()