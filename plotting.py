import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_driver_comparison(x1,x2,y1,y2,driver1,driver2):
    plt.plot(x1,y1,label=driver1)
    plt.plot(x2,y2,label=driver2)
    plt.title("Comparison")
    plt.show()
    