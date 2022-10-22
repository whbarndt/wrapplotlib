from turtle import color
import src.wrapplotlib as wrap
from matplotlib.testing.compare import compare_images
import matplotlib.pyplot as plt
import numpy as np
import os

# Testing Threshold
thrshld = 0.0001

# Testing the Bar Plot Demo
def test_plot_bar_demo():
    ### TEST IMAGE ###
    test_image = "./plot_bar_demo_test.png"
    wrap.plot(showfig=False, savefig=True, savefigname=test_image)

    ### REFERENCE IMAGE ###
    reference_image = "./plot_bar_demo.png"
    # Figure Definition
    fig, ax = plt.subplots(figsize=(wrap.default_bar_args['figure_width'], wrap.default_bar_args['figure_height']))
    # Defaults
    ax.set_title('Students enrolled in different courses')
    ax.set_xlabel('Courses offered')  
    ax.set_ylabel('No. of students enrolled')
    ax.tick_params(axis='x', labelsize=wrap.default_bar_args['ticklabelsize'])
    ax.tick_params(axis='y', labelsize=wrap.default_bar_args['ticklabelsize'])
    # Plot
    ax.plot(wrap.bar_demo_x, wrap.bar_demo_y, color='maroon')
    plt.savefig(reference_image)
    
    assert compare_images(reference_image, test_image, thrshld) == None
    #os.remove(test_image)
    #os.remove(reference_image)

# Testing the 2D Plot Demo
def test_plot_2dplot_demo():
    
    ### TEST IMAGE ###
    test_image = "./plot_2dplot_demo_test.png"
    # function_with_custom_labels.png - test
    wrap.plot(type='2dplot', showfig=False, savefig=True, savefigname=test_image)
    
    ### REFERENCE IMAGE ###
    reference_image = "./plot_2dplot_demo.png"
    # Figure Definition
    fig, ax = plt.subplots(figsize=(wrap.default_plot_args['figure_width'], wrap.default_plot_args['figure_height']))
    # Defaults
    ax.set_title('Plot of Sine(x) from 0 to 2pi')
    ax.set_xlabel(wrap.default_plot_args['xlabel'])  
    ax.set_ylabel(wrap.default_plot_args['ylabel'])
    ax.tick_params(axis='x', labelsize=wrap.default_plot_args['ticklabelsize'])
    ax.tick_params(axis='y', labelsize=wrap.default_plot_args['ticklabelsize'])
    # Plot
    ax.plot(wrap.plot_demo_x, wrap.plot_demo_y, color=wrap.default_plot_args['color'])
    plt.savefig(reference_image)
    
    assert compare_images(reference_image, test_image, thrshld) == None
    #os.remove(test_image)
    #os.remove(reference_image)