from __future__ import division
from matplotlib import pyplot as plt
import numpy as np


with open('millikan.txt', 'r') as datafile:
    freqs, volts = np.loadtxt(datafile, unpack=True)
    freqs = np.array(freqs)
    volts = np.array(volts)

N = len(freqs)
assert N==len(volts)

Ex = 1/N * np.sum(freqs)
Ey = 1/N * np.sum(volts)
Exx = 1/N * np.sum(freqs**2)
Exy = 1/N * np.sum(freqs*volts)

m = (Exy - Ex*Ey)/(Exx - Ex**2)
c = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)
print m
print c

plt.plot(freqs, volts, marker='.', linestyle='')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage (V)')
plt.show()

