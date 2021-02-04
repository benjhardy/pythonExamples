# Taken from 
# https://medium.com/swlh/calculating-the-convolution-of-two-functions-with-python-8944e56f5664
# imports
import matplotlib.pyplot as plt
import numpy as np
import math
def f(x):
    if -.7 < x < .7:
        return(1)
    else:
        return(0)

def convo(x):
    fog=0
    xt=-5
    dx=0.01
    while xt<5:
        fog=fog+f(xt)*g(x-xt)*dx
        xt=xt+dx
    return(fog)

def g(x):
    return(math.exp((-x**2)/(2*.3**2)))

t = -5
dt = 0.005
ff = np.empty(0)
tt = np.empty(0)
fg = np.empty(0)
gg = np.empty(0)

while t<5:
    tt = np.append(tt, t)
    ff = np.append(ff, f(t))
    fg = np.append(fg, convo(t))
    gg = np.append(gg, g(t))
    t=t+dt

plt.plot(tt,ff,tt,gg,tt,fg)
plt.show()

dx = 0.005
x = -3
xx = np.empty(0)
cc = np.empty(0)

# This is Hilariously Slow
plt.ion()
plt.plot(tt,ff)
plt.draw()
while x < 3:
    
    data = np.empty(0)
    ttt = np.empty(0)
    t = -3
    xx = np.append(xx,x)
    cc = np.append(cc,convo(x))
    while t<3:
        data = np.append(data,g(t-x))
        ttt = np.append(ttt,t)
        t = t+dt
    # plot continously the convolution
    plt.gca().cla()
    plt.plot(ttt, data)
    plt.draw()
    plt.plot(xx,cc)
    plt.draw()
    plt.pause(0.0001)
    plt.gca().cla()
    # plot moving function, which is data
    x = x+dx
plt.show(block=True)