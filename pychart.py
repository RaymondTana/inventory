import numpy as np
import matplotlib.pyplot as plt
#  %matplotlib inline

def create_pychart(labels, values, colors, title):
    sum_values = sum(v for v in values)
    percentages = [v / sum_values for v in values]
    slices = [None] * len(labels)
    class Slice:
        def __init__(self, label, value, percentage, color):
            self.label = label
            self.value = value
            self.percentage = percentage
            self.color = color

    for i in range(len(labels)):
        slices[i] = Slice(labels[i], values[i], percentages[i], colors[i])

    slices = sorted(slices, key=lambda x: x.value, reverse=False)

    large = slices[:len(slices) // 2]
    small = slices[len(slices) // 2:]

    reordered = large[::2] + small[::2] + large[1::2] + small[1::2]
    explode = [0.03] * len(labels)

    fig = plt.figure(figsize=[10, 10])
    ax = fig.add_subplot(111)

    angle = 180 + 360 * float(sum(s.value for s in small)) / sum(s.value for s in reordered)

    pie_wedge_collection, text = ax.pie([s.value for s in reordered], labels=["" if s.percentage < 0.005 else s.label for s in reordered], colors=[s.color for s in reordered], labeldistance=1.05, startangle=angle, explode=explode, shadow=True, radius=1.2);
    [ _.set_fontsize(20) for _ in text ]

    ax.set_title(title, fontsize = 30);

    plt.legend(reversed(pie_wedge_collection), reversed([s.label + " (" + str(round(s.percentage * 1000) / 10) + "%)" for s in reordered]), loc='best', bbox_to_anchor=(-0.1, 1.), fontsize=14)
    # plt.legend(pie_wedge_collection, [s.label for s in reordered], loc='best', bbox_to_anchor=(-0.1, 1.), fontsize=14)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def create_barh(labels, values, color, y_label, x_label, title):
    pos = [i for i, _ in enumerate(labels)]

    plt.figure(figsize=(7, 7))
    plt.ylabel(y_label, fontsize = 15)
    plt.xlabel(x_label, fontsize = 15)
    plt.title(title, fontsize = 22)
    plt.grid(zorder=0)
    plt.barh(pos, values, color=color, zorder=3)
    plt.yticks(pos, labels)

    plt.show()