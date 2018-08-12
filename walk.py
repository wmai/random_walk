# -*- coding: utf-8 -*-
# @Author: wmai
# @Date:   2018-07-30 19:23:37
# @Last Modified by:   William Mai
# @Last Modified time: 2018-08-12 02:04:06

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

import matplotlib.pyplot as plt
import random


iterations = 50
colors = ['#0F0BAF', '#0F0BAF', '#0F0BAF', '#0F0BAF', '#ED3B49']
widths = [0.1, 0.2, 0.2, 0.4, 0.5]
max_size = 100
hash = random.getrandbits(128)


def generate_walk(length):
    # We get the startig position of the walk
    x, y = random.randint(-50, 50), random.randint(-50, 50)
    walk_x = [x]
    walk_y = [y]

    for i in range(length):
        direction = random.choice(['N', 'W', 'S', 'E'])

        if direction == 'N':
            if (y + 1) < (960):
                y += 1
        elif direction == 'W':
            if (x + 1) < (470):
                x += 1
        elif direction == 'S':
            if (y - 1) > (960 * -1):
                y += -1
        elif direction == 'E':
            if (x - 1) > (470 * -1):
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
    walk = generate_walk(random.randint(100, 7000))
    config = generate_config()
    plt.plot(walk['x'], walk['y'], color=config['color'], linewidth=config['linewidth'])

plt.axis('off')
plt.savefig(dir_path + '/examples/example_' + str(hash) + '.png', bbox_inches=None, dpi=300)
plt.close()
