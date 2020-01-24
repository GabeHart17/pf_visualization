import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = 0
b = 2
x_dat = []
y_dat = []

fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro')

def init():
    global x_dat
    global y_dat
    global a
    global b
    global ln
    a = 0
    b = 2
    x_dat = []
    y_dat = []
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

def update(frame):
    global x_dat
    global y_dat
    global a
    global b
    global fig
    global ln
    if frame == 0:
        init()
        fig.clear()
    x_dat.append(a)
    y_dat.append(b)
    a += 0.2
    b += 0.1
    ln.set_data(x_dat, y_dat)
    return ln,

anim = FuncAnimation(fig, update, frames=range(10), init_func=init, blit=True, repeat=True, repeat_delay=1000)
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')
#
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
# plt.show()
