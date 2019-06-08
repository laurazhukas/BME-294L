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
frequency = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 10000]
Vo=[1.03, 1.02, 0.984, 0.968, 0.936, 0.888, 0.872, 0.816, 0.776, 0.752, 0.488, 0.280, 0.136]
ex_phase_shift = [-5.75, -11.5, -16.2, -21.3, -25.2, -29.1, -33.5, -38.0, -41.1, -43.2, -61.7, -74.1, -81.6]

Vo2 =[0.105, 0.204, 0.280, 0.368, 0.456, 0.512, 0.568, 0.624, 0.664, 0.704, 0.896, 0.984, 1.01]
ex_phase_shift2 = [86.1, 79.2, 75.0, 69.1, 63.2, 61.4, 56.4, 53.5, 49.5, 46, 27.7, 14.5, 5.21]

w = []
for i in range(len(frequency)):
    w.append(2*np.pi*frequency[i])

dB = 20*np.log10(Vo2)
# print(dB)

# slope, intercept = np.polyfit(np.log(dB), np.log(frequency), 1)
# print(slope)

#plot frequency against gain
plt.grid(which = 'both')
plt.plot(frequency, dB)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)') 
plt.xscale('log')

# plt.axhline(y=-3, c='g', linestyle = '-')
# plt.axvline(x = 1000, c = 'g', linestyle = "-")
# plt.axvline(x = 10000, c = 'r', linestyle = "-")
plt.show()

#plot phase degree against frequency
plt.grid(which = 'both')
plt.plot(frequency, ex_phase_shift2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Degree)') 
plt.xscale('log')
plt.show()