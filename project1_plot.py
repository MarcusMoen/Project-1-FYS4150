import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import math

matplotlib.rcParams.update({'font.size':14})

df = pd.read_csv('data.txt', sep=' ', header=None)
x = df[0].to_numpy()
u = df[1].to_numpy()

df = pd.read_csv('approx_with_10_xes.txt', sep=' ', header=None)
x1 = df[0].to_numpy()
v1 = df[1].to_numpy()

df = pd.read_csv('approx_with_100_xes.txt', sep=' ', header=None)
x2 = df[0].to_numpy()
v2 = df[1].to_numpy()

df = pd.read_csv('approx_with_1000_xes.txt', sep=' ', header=None)
x3 = df[0].to_numpy()
v3 = df[1].to_numpy()

fig, ax = plt.subplots(3,1, figsize=(8,12))

plt.suptitle('Poisson equation', fontsize=18)
plt.subplots_adjust(top=0.95)

ax[0].plot(x,u)
ax[0].plot(x1,v1)
ax[0].grid()
ax[0].set_xlabel('x')
ax[0].set_ylabel('u(x)')
ax[0].legend(['Real solution', 'Approximated solution \n with 10 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

ax[1].plot(x,u)
ax[1].plot(x2,v2)
ax[1].grid()
ax[1].set_xlabel('x')
ax[1].set_ylabel('u(x)')
ax[1].legend(['Real solution', 'Approximated solution \n with 100 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

ax[2].plot(x,u)
ax[2].plot(x3,v3)
ax[2].grid()
ax[2].set_xlabel('x')
ax[2].set_ylabel('u(x)')
ax[2].legend(['Real solution', 'Approximated solution \n with 1000 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

plt.savefig('poisson.pdf', dpi=900)
plt.show()




#Task 8a
def absolute_log_error(u, v):
    abs_error = []
    for i in range(len(u)):
        abs_error.append(math.log10(abs(u[i]-v[i])))
    return abs_error

#Task 8b
def relative_log_error(u, v):
    abs_error = []
    for i in range(len(u)):
        abs_error.append(math.log10(abs((u[i]-v[i])/u[i])))
    return abs_error
