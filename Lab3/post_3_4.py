# Part 3.2
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

R = 4700
C = 0.000000033
Tau = R*C
Vi = 1 #voltage peak to peak
frequency = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
circuit3_measured_gain = [0.504, 0.504, 0.504, 0.508, 0.508, 0.484, 0.440, 0.167, 0.0892]
theoretical_gain = [-6.107, -6.107, -6.107, -6.111, -6.122, -6.471, -7.408, -15.99, -21.66]

w = []
for i in range(len(frequency)):
    w.append(2*np.pi*frequency[i])

dB = 20*np.log10(circuit3_measured_gain)
# print(dB)


#plot frequency against gain
plt.grid(which = 'both')
plt.plot(frequency, dB)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Measured Gain (dB)') 
plt.xscale('log')

plt.axhline(y=-9, c='g', linestyle = '-')
# plt.axvline(x = 1000, c = 'g', linestyle = "-")
# plt.axvline(x = 10000, c = 'r', linestyle = "-")
plt.show()

plt.axhline(y=-9, c='g', linestyle = '-')
#plot phase degree against frequency
plt.grid(which = 'both')
plt.plot(frequency, theoretical_gain)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Theoretical Gain (dB)') 
plt.xscale('log')
plt.show()