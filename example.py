import matplotlib.pyplot as plt
import numpy as np
import datetime
#import pandas

# label='t = '+str(t[i])
def plot(x, y, axis_labels=['x','y'], legend=False, tick_label_size='small'):
    # Defaults
    default_axis_labels = ['x','y']
    default_tick_font_size = 10
    default_figure_size = (12,8)

    # Figure and Plot Definition
    fig, ax = plt.subplots(figsize=default_figure_size)

    # Setting Axis Labels
    #plt.xlabel(axis_labels[0]) 
    #plt.ylabel(axis_labels[1])
    ax.set_xlabel(axis_labels[0])  
    ax.set_ylabel(axis_labels[1])

    # Legend
    if legend is True:
        plt.legend()

    # Datetime Labels
    if datetime.datetime in x:
        ax.xaxis.set_major_formatter(mdates.DateFormatter(partdatenameformat))

    # Tick Sizes
    def set_tick_size(fontsize):
        ax.tick_params(axis='x', labelsize=fontsize)
        ax.tick_params(axis='y', labelsize=fontsize)
    if tick_label_size == 'large':
        set_tick_size(25)
    elif tick_label_size == 'medium':
        set_tick_size(17.5)
    elif tick_label_size == 'small':
        set_tick_size(10)

    # Plot and Save Figure
    ax.plot(x, y)
    #savefig('plot.png', transparent=True)
    #plt.show()
    return

'''
# Wave Parameters:
A = 1           # Amplitude
k = 2           # Wavenumber 
w = np.pi       # Angular Frequency
T = 2*np.pi/w   # Period

# Spatial and Temporal Data
x = np.linspace(0,2*np.pi,100)
#t = np.array([0, T/5, T/4])
t = 0
labels=['x', 'f(x)']
# Plotting
#for i in range(len(t)):
y = A*np.cos(k*x-w*t)
plot(x, y, axis_labels=labels)
'''
