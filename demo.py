import src.wrapplotlib as wrap
import numpy as np

# Bar Test
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]

params = {
    'title': 'Fruit supply by kind and color',
    'ylabel': 'fruit supply',
    'legend': True,
    'legend_title': 'Fruit color',
    'bar_labels': ['red', 'blue', '_red', 'orange'],
    'custom_bar_colors': ['tab:red', 'tab:blue', 'tab:red', 'tab:orange'],
}

# wrap.plot()
wrap.plot(fruits, counts, type='bar', args=params)  # type: ignore

# Plot Test
x = np.linspace(0, 2*np.pi)
y = np.tan(x)

# wrap.plot(type='2dplot')
# wrap.plot(x, y, type='2dplot')
