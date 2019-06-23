# Prelab
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

R = 18000
C = 0.00000001201

def calculate_gain(R, C, w):
    computed = []
    for i in range(len(w)):
        computed.append(1/(np.sqrt(4*np.power(np.pi, 2)*np.power(w[i], 2)*np.power(C, 2) * np.power(R, 2) +1)))
    return np.asarray(computed)

w = np.linspace(10, 10000, 100000)
dB = []
dB = 20*np.log10(calculate_gain(R, C, w))

plt.plot(w, dB)
plt.grid(which = 'both')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)') 
plt.xscale('log')
plt.show()
