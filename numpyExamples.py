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
# plt.plot(freq, np.convolve(Y1,Y2))
# plt.show()

# Fourier Transform example with np
# Source : https://pythontic.com/visualization/signals/fouriertransform_fft
#sampling frequency
df = 100 # Hz
# time points
ds = 1/df # (s)
# begin time
beginTime = 0
endTime = 10
# Frequencies
freq1 = 4
freq2 = 7

time = np.arange(beginTime,endTime,ds)
s1 = np.sin(2*np.pi*freq1*time)
s2 = np.sin(2*np.pi*freq2*time)

# Create subplot
figure, axis = plt.subplots(4,1)
plt.subplots_adjust(hspace=1)

# Time domain rep
axis[0].set_title('Sine Wave with a frequency of 4Hz')
axis[0].plot(time,s1)
axis[0].set_xlabel('Time (s)')
axis[0].set_ylabel('Amplitude (arb.)')

# time domain sine wave 2
axis[1].set_title('Sine Wave with a frequency of 7Hz')
axis[1].plot(time,s2)
axis[1].set_xlabel('Time (s)')
axis[1].set_ylabel('Amplitude (arb.)')

s3 = s1+s2
axis[2].set_title('Sum of two signals')
axis[2].plot(time,s3)
axis[2].set_xlabel('Time (s)')
axis[2].set_ylabel('Amplitude (arb.)')

# freq. domain representation...
ft = np.fft.fft(s3) # normalize amplitude
print(len(ft))
#ft = ft[range(int(len(s3)/2))]

tpCount = len(s3)
values = np.arange(int(tpCount/2))
timePeriod = tpCount/df
frequencies = values/timePeriod

axis[3].set_title('Freq. Domain Representation')
axis[3].plot(np.abs(ft))
axis[3].set_xlabel('Frequency (Hz)')
axis[3].set_ylabel('Amplitude (arb.)')

plt.show()