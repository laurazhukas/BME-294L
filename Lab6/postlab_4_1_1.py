import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

frequency = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 10000]
Vo = [2.02, 1.96, 1.84, 1.7, 1.58, 1.46, 1.34, 1.24, 1.14, 1.06, 0.620, 0.304, 0.12]
Vo_2= [2.04, 2.03, 2.01, 1.92, 1.7, 1.6, 1.43, 1.35, 1.21, 1.07, 0.258, 0.079, 0.0147]
Vi = 2

gain =[]
for i in range(len(Vo)):
    gain.append(Vo_2[i]/Vi)

gain_dB = []
for i in range(len(gain)):
    gain_dB.append(20*np.log10(gain[i]))

print(gain)
print(gain_dB)

plt.grid(which = 'both')
plt.plot(frequency, gain_dB)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)') 
plt.xscale('log')
# plt.title('First-Order Low-Pass Filter')
plt.title('Second-Order Low-Pass Filter')
plt.show()