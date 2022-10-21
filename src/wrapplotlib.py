# Bar Chart and Plot (Wrapper Example)
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import datetime as dt

default_bar_args = {
    'figure_height': 8,
    'figure_width': 12,
    'title': 'Bar Chart',
    'titlefontsize': 30,
    'xlabel': 'X Axis',
    'ylabel': 'Y Axis',
    'axislabelsize': 20,
    'ticklabelsize': 'medium',
    'bar_colors': 'maroon',
    'edgecolor': 'black',
    'linewidth': 0.7,
    'legend': False,
    'legend_title': 'Legend',
    'custom_bar_labels': None,
    'transparent': False,
}

default_plot_args = {
    'figure_height': 8,
    'figure_width': 12,
    'title': "2D Plot",
    'titlefontsize': 30,
    'xlabel': 'x',
    'ylabel': 'f(x)',
    'axislabelsize': 20,
    'ticklabelsize': 'medium',
    'color': 'green',
    'linewidth': 2,
    'legend': False,
    'legend_title': 'Legend',
    'datetimeformat': '%b-%d',
    'scale_x': True,
    'scale_y': True,
    'transparent': False,
}

# Bar Plot Demo Variables:
bar_demo_x = ['C', 'C++', 'Java', 'Python', 'Rust']
bar_demo_y = [15, 30, 20, 35, 75]

# 2D Plot Demo Variables:
plot_demo_x = np.linspace(0, 2*np.pi)
plot_demo_y = np.sin(plot_demo_x)

def plot(x = np.ones(1), y = np.ones(1), type='bar', args=default_bar_args, showfig=True, savefig=False, savefigname="default.png"):
   
    ## Bar Chart
    if type == 'bar':
        # Demo Condition
        if all(x) == True and all(y) == True:
            x = bar_demo_x
            y = bar_demo_y
            args['title'] = 'Students enrolled in different courses'
            args['xlabel'] = 'Courses offered'
            args['ylabel'] = 'No. of students enrolled'
        fig, ax = plt.subplots(figsize=(args['figure_width'], args['figure_height']))
        plot = ax.bar(x, y, label=args['custom_bar_labels'], color=args['bar_colors'])
    
    ## 2D Plot
    elif type == '2dplot':
        args = default_plot_args
        # Demo Condition
        if all(x) == True and all(y) == True:
            x = plot_demo_x
            y = plot_demo_y
            args['title'] = 'Plot of Sine(x) from 0 to 2pi'
        fig, ax = plt.subplots(figsize=(args['figure_width'], args['figure_height']))
        plot = ax.plot(x, y, color=args['color'])
        # Date Time Format Setting
        if dt.datetime in x:
            ax.xaxis.set_major_formatter(mdates.DateFormatter(args['datetime-format']))
    
    ## Universal Settings
    
    # Title, x and y label
    ax.set_title(args['title'], fontsize=args['titlefontsize'])
    ax.set_xlabel(args['xlabel'], fontsize=args['axislabelsize'])
    ax.set_ylabel(args['ylabel'], fontsize=args['axislabelsize'])
    # Legend
    if args['legend'] is True:
        ax.legend()
    # Axis Tick Labels Setting
    def set_xy_ticksize(num):
        ax.tick_params(axis='x', labelsize=num)
        ax.tick_params(axis='y', labelsize=num)
    if isinstance(args['ticklabelsize'], str):
        if args['ticklabelsize'] == 'large':
            set_xy_ticksize(25)
        elif args['ticklabelsize'] == 'medium':
            set_xy_ticksize(20)
        elif args['ticklabelsize'] == 'small':
            set_xy_ticksize(15)
    else:
        set_xy_ticksize(args['ticklabelsize'])
    # Save Figure Settings
    if savefig:
        plt.savefig(savefigname, transparent=args['transparent'])
    if showfig:
        plt.show()
    return plot
