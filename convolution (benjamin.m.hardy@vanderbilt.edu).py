# imports
import numpy as np
import math
import matplotlib.pyplot as plt
# Functions
def plot2Arrays(x,y1,y2):
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.suptitle('Functions')
    ax1.plot(x,y1)
    ax2.plot(x,y2)
    plt.show()
    
# show the Convolution Theorem is True by creating two functions and...
# multiplying them in conjugate space, and convoluting them in the original space...

# Two Functions
t = np.linspace(-5, 5, 101)

print(t.shape[-1])
y1 = np.sinc(t)
y2 = np.heaviside(t,.5)


# example plots
# plt.plot(t,y1)
# plt.plot(t,y2)

# plt.ylabel('Sinc Function')
# plt.xlabel('Time (ns)')
# plt.show()

plot2Arrays(t,y1,y2)

# Fourier Transform the data <==>
freq = np.fft.fftfreq(t.shape[-1],t[2]-t[1])
Y1 = np.fft.fft(y1)
Y2 = np.fft.fft(y2)


plt.plot(freq, Y2.real, freq, Y1.real)
plt.show()

# Multiply them
plt.plot(t,y1*y2)
plt.show()

# Convolve them
plt.plot(freq, np.convolve(Y1,Y2))
plt.show()

