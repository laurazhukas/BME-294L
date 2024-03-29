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

w = []
for i in range(len(frequency)):
    w.append(2*np.pi*frequency[i])

Vo=[]
# circuit 1 - Figure 3.1, low pass filter
# for i in range(len(frequency)):
#     Vo.append(1/np.sqrt((np.power(w[i], 2)*np.power(Tau, 2)+1)))

# circuit 2 - Figure 3.2, high pass filter
for i in range(len(frequency)):
    Vo.append((w[i]*Tau)/np.sqrt((1+np.power(Tau,2)*np.power(w[i],2))))
# print(Vo)

voltage_gain = []
# circuit 1
# for i in range(len(w)):
#     voltage_gain.append(1/(np.sqrt(np.power(w[i], 2)*np.power(Tau,2)+1)))
#circuit 2
for i in range(len(w)):
    voltage_gain.append((w[i]*Tau)/np.sqrt((1+np.power(Tau,2)*np.power(w[i],2))))

# print(voltage_gain)

phase_shift =[]
phase_shift_degrees = []
# circuit 1
# for i in range(len(frequency)):
#     phase_shift.append(np.arctan((-w[i]*Tau)))
#     phase_shift_degrees.append((180/np.pi)*np.arctan((-w[i]*Tau))) 
# circuit 2
for i in range(len(frequency)):
    phase_shift.append(np.arctan((-w[i]*Tau)))
    phase_shift_degrees.append((180/np.pi)*np.arctan((1/(w[i]*Tau)))) 

# print(phase_shift)
# print(phase_shift_degrees)

dB = 20*np.log10(voltage_gain)
# print(dB)


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
plt.plot(frequency, phase_shift_degrees)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Degree)') 
plt.xscale('log')
plt.show()