import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_driver_comparison(x1,x2,y1,y2):
    plt.plot(np.array(x1),np.array(y1))
    plt.plot(np.array(x2),np.array(y2))
    plt.title("Comparison")
    plt.show()
    