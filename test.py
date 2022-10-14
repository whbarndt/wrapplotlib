import example as ex
from matplotlib.testing.decorators import image_comparison
from matplotlib.testing.compare import compare_images
import matplotlib.pyplot as plt
import numpy as np

# Testing Threshold
thrshld = 0.0001

# Plot Data
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

# Plot Function Defaults
default_axis_labels = ['x','y']
default_tick_font_size = 10
default_figure_size = (12,8)

def test_function_default():
    ### TEST IMAGE ###
    test_image = "./result_images/test/function_default.png"
    ex.plot(x, y)
    plt.savefig(test_image)

    ### REFERENCE IMAGE ###
    reference_image = "./baseline_images/test/function_default.png"
    # Figure Definition
    fig, ax = plt.subplots(figsize=default_figure_size)
    # Defaults
    ax.set_xlabel(default_axis_labels[0])  
    ax.set_ylabel(default_axis_labels[1])
    ax.tick_params(axis='x', labelsize=default_tick_font_size)
    ax.tick_params(axis='y', labelsize=default_tick_font_size)
    # Plot
    ax.plot(x, y)
    plt.savefig(reference_image)
    
    assert compare_images(reference_image, test_image, thrshld) == None

def test_function_with_custom_labels():
    custom_labels=['x', 'f(x)']
    
    ### TEST IMAGE ###
    test_image = "./result_images/test/function_with_custom_labels.png"
    # function_with_custom_labels.png - test
    ex.plot(x, y, axis_labels=custom_labels)
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
    
    assert compare_images(reference_image, test_image, thrshld) == None