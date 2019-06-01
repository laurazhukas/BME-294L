import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

R2 = 500
R3 = 10000
C4 = 0.000047

def oOverIVoltage(R2, R3, C4, w):
    #R3/(j*w*C4*R3*R2+R3+R2), j is imaginary, not inculded
    computed = []
    for i in range(len(w)):
        computed.append(abs(R3/(w[i]*C4*R3*R2+R3+R2))) 
    return np.asarray(computed)

w = np.linspace(0.001, 1000, 1000000)*(2*np.pi)
print(type(w))
dB = []
dB = 20*np.log10(oOverIVoltage(R2, R3, C4, w))
plt.plot(w, dB)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)') 
plt.xscale('log')
plt.show()