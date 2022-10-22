# Bar Chart and Plot (Wrapper Example)
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import datetime as dt
import copy

default_bar_args = {
    'figure_height': 8,
    'figure_width': 12,
    'title': 'Bar Chart',
    'titlefontsize': 30,
    'xlabel': 'X Axis',
    'ylabel': 'Y Axis',
    'axislabelsize': 20,
    'ticklabelsize': 'medium',
    'custom_bar_colors': 'maroon',
    'edgecolor': 'black',
    'linewidth': 0.7,
    'legend': False,
    'legend_title': 'Legend',
    'transparent': False,
    'bar_labels': None,   
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

# Updates passed in dictionary - allows for variable amount of arguments to be passed
def get_updated_dict(given_dict, set_dict):
    set_key_list = list(set_dict.keys())
    given_key_list = list(given_dict.keys())
    new_dict = copy.deepcopy(set_dict)
    for i in set_key_list:
        for j in given_key_list:
            if i == j:
                new_dict[i] = given_dict[j]
    return new_dict

def plot(x = np.zeros(5), y = np.zeros(5), type='bar', args=default_bar_args, showfig=True, savefig=False, savefigname="default.png"):
   
    ## Bar Chart
    if type == 'bar':
        args = get_updated_dict(args, default_bar_args)
        # Demo Condition
        if np.array_equal(x, np.zeros(5)) and np.array_equal(y, np.zeros(5)):
            x = bar_demo_x
            y = bar_demo_y
            args['title'] = 'Students enrolled in different courses'
            args['xlabel'] = 'Courses offered'
            args['ylabel'] = 'No. of students enrolled'
        fig, ax = plt.subplots(figsize=(args['figure_width'], args['figure_height']))
        plot = ax.bar(x, y, label=args['bar_labels'], color=args['custom_bar_colors'])
    
    ## 2D Plot
    elif type == '2dplot':
        args = get_updated_dict(args, default_plot_args)
        # Demo Condition
        if np.array_equal(x, np.zeros(5)) and np.array_equal(y, np.zeros(5)):
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
        ax.legend(title=args['legend_title'])
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