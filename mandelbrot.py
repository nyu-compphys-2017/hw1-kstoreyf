from matplotlib import pyplot as plt
import numpy as np


def mandelbrot(z, c):
    zp = z**2 + c
    return zp

def iterate(c):
    print c
    counter = 0
    max = 10
    zp = mandelbrot(0, c)
    print zp
    while abs(zp) <= 2:
        zp = mandelbrot(zp, c)
        print zp
        counter += 1
        if counter > max:
            return True
    return False

def image(N=10):
    max = 2
    min = -2
    ns = np.linspace(min, max, N)
    print ns
    inset = []
    outset = []
    for x in ns:
        for y in ns:
            c = complex(x, y)
            man = iterate(c)
            if man:
                inset.append([x,y])
            else:
                outset.append([x,y])
    plt.plot(inset, marker='.', linestyle='', color='black')
    plt.plot(outset, marker='.', linestyle='', color='cyan')
    plt.show()


if __name__=='__main__':
    image()