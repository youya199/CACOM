# Import packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def visual(list_of_angles):
    # Create figure and add axes
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_xlabel('time')
    ax.set_ylabel('angle')

    # time values
    epo=len(list_of_angles)
    T = np.linspace(0, epo*1/240, epo)
    # angle values
    A=list_of_angles

    # Create  plot
    ax.plot(T, A, linewidth=2.5)
