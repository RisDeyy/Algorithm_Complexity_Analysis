import math
import matplotlib.pyplot as plt

def plot_diagonal(ax, color):
    length = math.sqrt(200**2 + 1000**2)
    # unpack the first point
    x, y = (0,0)

    width = ax.get_xlim()[1]
    height = ax.get_ylim()[1]

    # find the end point
    endx = x + length * width / length
    endy = y + length * height / length

    ax.plot([x, endx], [y, endy], color=color)