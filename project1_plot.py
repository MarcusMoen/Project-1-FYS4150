import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import math

matplotlib.rcParams.update({'font.size':14})

df = pd.read_csv('data.txt', sep=' ', header=None)
x = df[0].to_numpy()
u = df[1].to_numpy()

df = pd.read_csv('test.txt', sep=' ', header=None)
x2 = df[0].to_numpy()
v = df[1].to_numpy()

plt.plot(x,u)
plt.plot(x2,v)
plt.grid()
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Poisson equation')
plt.savefig('poisson1.pdf', dpi=900)


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
    
    
