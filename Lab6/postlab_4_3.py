import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# frequency = [50, 100, 200, 500, 2000, 5000, 10000, 20000]
Vo= [0.010, 0.02, 0.0212, 0.124, 0.15, 0.048, 0.02, 0.0152]
Vi = 2

gain =[]
for i in range(len(Vo)):
    gain.append(Vo[i]/Vi)

frequency = [50, 100, 200, 500, 800, 1000, 1130, 2000, 5000, 10000, 20000]
altered_gain = [-46.020599913279625, -40.0, -39.493882694704595, -24.15216621003492, -10, -3, -3, -22.498774732165998, -32.39577516576788, -40.0, -42.3872815438417]

gain_dB = []
for i in range(len(gain)):
    gain_dB.append(20*np.log10(gain[i]))


print(gain)
print(gain_dB)

plt.grid(which = 'both')
# plt.plot(frequency, gain_dB)
plt.plot(frequency, altered_gain)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)') 
plt.xscale('log')
plt.title('Bandpass Filter')
plt.show()