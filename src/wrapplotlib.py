# Bar Chart (Wrapper Example)

import matplotlib.pyplot as plt

args = {
    'title': 'Bar Chart',
    'xlabel': 'X Axis',
    'ylabel': 'Y Axis',
    'color': 'blue',
    'height': 5,
    'width': 10,
}

def plot(x, y, args):
    plt.figure(figsize=(args['width'], args['height']))
    plt.bar(x, y, color=args['color'])
    plt.title(args['title'])
    plt.xlabel(args['xlabel'])
    plt.ylabel(args['ylabel'])
    plt.show()
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()
