import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import random

def draw_colors(a, b, c):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.add_patch(
        patches.Rectangle(
            (0, 0.5), 0.5, 0.5,
            facecolor=a
        )
    )
    ax.add_patch(
        patches.Rectangle(
            (0.5, 0.5), 0.5, 0.5,
            facecolor=b
        )
    )
    ax.add_patch(
        patches.Rectangle(
            (0.0, 0), 1, 0.5,
            facecolor=c
        )
    )

def rgb_to_hex(rgb):
    return "#" + "".join(map(lambda x: "%02x" % min(x, 255), rgb))

def hex_to_rgb(hexc):
    return list(map(lambda x: int(x, 16), [hexc[1:3], hexc[3:5], hexc[5:7]]))

def random_color(rgb):
    return rgb_to_hex([random.randint(0, 256) for i in range(3)])

def mix_colors(rgba, rgbb):
    colorsA = hex_to_rgb(rgba)
    colorsB = hex_to_rgb(rgbb)
    return rgb_to_hex([int((colorsA[i] + colorsB[i]) / 2) for i in range(3)])

# Dump random colors as to colors.json
if __name__ == "__main__":
    data = []
    for i in range(10000):
        colorsA = [random.randint(0, 256) for i in range(3)]
        colorsB = [random.randint(0, 256) for i in range(3)]
        mix = [int((colorsA[i] + colorsB[i]) / 2) for i in range(3)]
        data.append(list(map(rgb_to_hex, [colorsA, colorsB, mix])))
    with open("colors.json", "w") as f:
        json.dump(data, f, indent=2)
