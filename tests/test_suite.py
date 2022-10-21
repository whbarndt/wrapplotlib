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

'''def test_function_with_custom_labels():
    custom_labels=['x', 'f(x)']
    
    ### TEST IMAGE ###
    test_image = "./result_images/test/function_with_custom_labels.png"
    # function_with_custom_labels.png - test
    wrap.plot(x, y, axis_labels=custom_labels)
    plt.savefig(test_image)
    
    ### REFERENCE IMAGE ###
    reference_image = "./baseline_images/test/function_default.png"
    # Figure Definition
    fig, ax = plt.subplots(figsize=default_figure_size)
    # Defaults
    ax.tick_params(axis='x', labelsize=default_tick_font_size)
    ax.tick_params(axis='y', labelsize=default_tick_font_size)
    ## Customizations ##
    ax.set_xlabel(custom_labels[0])
    ax.set_ylabel(custom_labels[1])
    # Plot
    ax.plot(x, y)
    plt.savefig(reference_image)
    
    assert compare_images(reference_image, test_image, thrshld) == None'''