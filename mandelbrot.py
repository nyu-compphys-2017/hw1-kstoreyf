from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np


# Calculate the Mandelbrot function
def mandelbrot(z, c):
    zp = z**2 + c
    return zp

# Iterate on each z value with the Mandelbrot function
# Return true for in the Mandelbrot set, false for not in set
def iterate(c, xmax):
    counter = 0
    max = 100
    zp = mandelbrot(0, c)
    while abs(zp) <= xmax:
        zp = mandelbrot(zp, c)
        counter += 1
        if counter > max:
            return True, max
    return False, counter

# Create image using the Mandelbrot fractal using an NxN grid
def image(N=100):
    xmax = 2
    xmin = -xmax
    ns = np.linspace(xmin, xmax, N)
    insetx = []
    outsetx = []
    insety = []
    outsety = []
    outsetcols = []
    for x in ns:
        for y in ns:
            c = complex(x, y)
            man, num = iterate(c, xmax)

            if man:
                insetx.append(x)
                insety.append(y)
            else:
                outsetx.append(x)
                outsety.append(y)
                outsetcols.append(np.log10(num+1))

    plt.scatter(insetx, insety, marker='.', edgecolor='', c='black')
    plt.scatter(outsetx, outsety, marker='.', edgecolor='', c=outsetcols, cmap=cm.plasma)
    cbar = plt.colorbar()
    cbar.set_label('log(# of iterations)')

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()


if __name__=='__main__':
    image()