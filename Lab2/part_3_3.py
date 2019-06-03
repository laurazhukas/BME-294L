import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

frequency = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
w = []
for i in range(len(frequency)):
    w.append(2*np.pi*frequency[i])

eqtn = []
part1 = 2*np.power(10,10)
for i in range(len(w)):
    # eqtn.append(20*np.log10((2*10**10)/np.sqrt((4.04*10**10)**2 + w[i]**2 * 38000**2)))
    # part2 = np.sqrt(np.power((4.04*np.power(10,10)),2) + np.power(w[i],2) * np.power(38000,2))
    # eqtn.append(20*np.log10(part1/part2))
    eqtn.append(20*np.log10((2*np.power(10,10))/(np.sqrt(np.power((4.04*np.power(10,10)),2) + np.power(w[i],2) * np.power(38000,2)))))

# Zeq = []
# for i in range(len(w)):
#     Zeq.append(1/np.sqrt((1/19607)**2 + (w[i]*95*(10**-12))**2))

# Vo =[]
# for i in range(len(w)):
#     Vo.append(20*np.log10(Zeq[i]/(Zeq[i]+20*(10**3))))

print(eqtn)
# print(Vo)
