import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from animated_data_loader import AnimatedDataLoader
import math


with open(sys.argv[1]) as f:
    data = AnimatedDataLoader(f.read());

x_data = []
y_data = []
rot_data = []
beacon_x = [i[0] for i in data.beacons]
beacon_y = [i[1] for i in data.beacons]
predicted_x = []
predicted_y = []
actual_x = []
actual_y = []
error = []

fig, axes = plt.subplots(nrows=1, ncols=1)
ax = axes#[0]
# er = axes[1]
ax.plot(beacon_x, beacon_y, 'ko')
pln, = ax.plot([], [], 'r.')
aln, = ax.plot([], [], 'g.')
ln, = ax.plot([], [], 'b.')
# eln, = er.plot([], [], 'k-')

def set_data(iter):
    global x_data, y_data, rot_data, predicted_x, predicted_y, actual_x, actual_y
    x_data = []
    y_data = []
    rot_data = []
    for i in data.states[iter][0]:
        x_data.append(i[0])
        y_data.append(i[1])
        rot_data.append(i[2])
    predicted_x.append(data.states[iter][1][0])
    predicted_y.append(data.states[iter][1][1])
    actual_x.append(data.states[iter][-1][0])
    actual_y.append(data.states[iter][-1][1])
    error.append(math.hypot(predicted_x[-1] - actual_x[-1], predicted_y[-1] - actual_y[-1]))

def init():
    ax.set_xlim(data.field[0], data.field[1])
    ax.set_ylim(data.field[2], data.field[3])
    # er.set_xlim(0, len(data.states))
    # er.set_ylim(0, 2)
    set_data(0)
    return ln, pln, aln#, eln

def update(frame):
    if frame == 0:
        init()
    set_data(frame)
    pln.set_data(predicted_x, predicted_y)
    aln.set_data(actual_x, actual_y)
    ln.set_data(x_data, y_data)
    # eln.set_data(range(frame), error)
    return ln, pln, aln#, eln

anim = FuncAnimation(fig, update, frames=range(len(data.states)), init_func=init, blit=True, repeat=False, interval=200)
plt.show()
