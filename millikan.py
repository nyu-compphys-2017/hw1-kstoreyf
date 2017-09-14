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
print 'Slope:', m
print 'Intercept:', c

ys_lstsqs = []
for f in freqs:
    y = m*f + c
    ys_lstsqs.append(y)

e = 1.602e-19  # Charge of electron in Coulombs
h = m*e
print r'h =', h
realh = 6.626e-34
print '% from accepted h:',abs(realh-h)/realh

plt.plot(freqs, volts, marker='o', linestyle='', color='cyan', markeredgewidth=0,
         label='Millikan experimental data')
plt.plot(freqs, ys_lstsqs, marker='', linestyle='-', color='purple',
         label='Least squares fit')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage (V)')
plt.legend(loc='upper left', frameon=False, prop={'size':12})
plt.ylim(0, 3.5)
plt.show()

