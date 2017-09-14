from matplotlib import pyplot as plt
import numpy as np


with open('millikan.txt', 'r') as datafile:
    freqs, volts = np.loadtxt(datafile, unpack=True)

plt.plot(freqs, volts, marker='.', linestyle='')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage (V)')
plt.show()
