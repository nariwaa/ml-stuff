# %% Cell 1
import math
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
# %% Cell 2
def f(x):
    return 5*x**2 - 4*x + 5 + 2*x**3
# %% Cell
xs = np.arange(-5,5,0.25)
ys = f(xs)
plt.plot(xs, ys)
# %% Cell
h = 0.0000000000001
x = 3.0
f(x+h)
# 19 min end of part
