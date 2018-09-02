# -*- coding: utf-8 -*-
# @Author: wmai
# @Date:   2018-07-30 19:23:37
# @Last Modified by:   William Mai
# @Last Modified time: 2018-09-02 19:23:13

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

import matplotlib.pyplot as plt
import random
import datetime


iterations = 75
colors = ['#EC7500', '#EC7500', '#EC7500', '#EC7500', '#EC7500',
          '#EC7500', '#EC7500', '#4CAF50', '#2196F3', '#F44336']
widths = [0.01, 0.01, 0.02, 0.02, 0.025, 0.035, 0.045]
max_height = 1000
max_width = 100
ts = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
hash = random.getrandbits(128)
the_file = dir_path + '/results/' + str(ts) + '_' + str(hash) + '.svg'


def generate_walk(length):
    # We get the startig position of the walk
    x, y = random.randint(-max_width, max_width), random.randint(-max_height, max_height)
    walk_x = [x]
    walk_y = [y]

    for i in range(length):
        direction = random.choice(['N', 'W', 'S', 'E'])

        if direction == 'N':
            if (y + 1) < (max_height):
                y += 1
        elif direction == 'W':
            if (x + 1) < (max_width):
                x += 1
        elif direction == 'S':
            if (y - 1) > (max_height * -1):
                y += -1
        elif direction == 'E':
            if (x - 1) > (max_width * -1):
                x += -1

        walk_x.append(x)
        walk_y.append(y)

    return {'x': walk_x, 'y': walk_y}


def generate_config():
    color = random.choice(colors)
    linewidth = random.choice(widths)
    return {
        'color': color,
        'linewidth': linewidth,
    }


for i in range(iterations):
    walk = generate_walk(random.randint(50, 50000))
    config = generate_config()
    plt.plot(walk['x'],
             walk['y'],
             color=config['color'],
             linewidth=config['linewidth'])
    plt.tick_params(axis='both',
                    top=False,
                    bottom=False,
                    left=False,
                    right=False,
                    labeltop=False,
                    labelbottom=False,
                    labelleft=False,
                    labelright=False)


plt.axis('scaled')
plt.savefig(the_file,  bbox_inches='tight', pad_inches=0, dpi=80, frameon=False,
            tight_layout=0, orientation='portrait')
plt.close()

print('SVG file created : ' + the_file)
