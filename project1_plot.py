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
x1 = np.flip(df[0].to_numpy())
v1 = np.flip(df[1].to_numpy())

df = pd.read_csv('approx_with_100_xes.txt', sep=' ', header=None)
x2 = np.flip(df[0].to_numpy())
v2 = np.flip(df[1].to_numpy())

df = pd.read_csv('approx_with_1000_xes.txt', sep=' ', header=None)
x3 = np.flip(df[0].to_numpy())
v3 = np.flip(df[1].to_numpy())

df = pd.read_csv('approx_with_1000_xes.txt', sep=' ', header=None)
x4 = np.flip(df[0].to_numpy())
v4 = np.flip(df[1].to_numpy())

fig, ax = plt.subplots(2,2, figsize=(14,8))

plt.suptitle('Poisson equation', fontsize=18)
plt.subplots_adjust(top=0.9)

ax[0][0].plot(x,u)
ax[0][0].plot(x1,v1)
ax[0][0].grid()
ax[0][0].set_xlabel('x')
ax[0][0].set_ylabel('u(x)')
ax[0][0].legend(['Real solution', 'Approximated solution \n with 10 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

ax[0][1].plot(x,u)
ax[0][1].plot(x2,v2)
ax[0][1].grid()
ax[0][1].set_xlabel('x')
ax[0][1].set_ylabel('u(x)')
ax[0][1].legend(['Real solution', 'Approximated solution \n with 100 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

ax[1][0].plot(x,u)
ax[1][0].plot(x3,v3)
ax[1][0].grid()
ax[1][0].set_xlabel('x')
ax[1][0].set_ylabel('u(x)')
ax[1][0].legend(['Real solution', 'Approximated solution \n with 1000 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

ax[1][1].plot(x,u)
ax[1][1].plot(x4,v4)
ax[1][1].grid()
ax[1][1].set_xlabel('x')
ax[1][1].set_ylabel('u(x)')
ax[1][1].legend(['Real solution', 'Approximated solution \n with 10000 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

plt.savefig('poisson.pdf', dpi=900)
plt.show()



#Task 8a
def absolute_log_error(u, v):
    abs_error = [0]
    for i in range(len(u)-2):
        if u[i+1]-v[i+1] == 0:
            abs_error.append(0)
        else:
            abs_error.append(math.log10(abs(u[i+1]-v[i+1])))
    abs_error.append(0)
    return abs_error

#Task 8b
def relative_log_error(u, v):
    rel_error = [0]
    for i in range(len(u)-2):
        if u[i+1]-v[i+1] == 0:
            rel_error.append(0)
        else:
            rel_error.append(math.log10(abs((u[i+1]-v[i+1])/u[i+1])))
    rel_error.append(0)
    return rel_error

fig, ax = plt.subplots(2,1, figsize=(12,8))


plt.subplots_adjust(top=0.9)

ax[0].plot(x1,absolute_log_error(x1,v1), label='n = 10')
ax[0].plot(x2,absolute_log_error(x2,v2), label='n = 100')
ax[0].plot(x3,absolute_log_error(x3,v3), label='n = 1000')
ax[0].plot(x4,absolute_log_error(x4,v4), label='n = 10000')
ax[0].grid()
ax[0].set_title('Absolute error')
ax[0].set_xlabel('x')
ax[0].set_ylabel('Log Error')
ax[0].legend()#bbox_to_anchor = (0.57, 1), fontsize=12)


ax[1].plot(x1,relative_log_error(x1,v1), label='n = 10')
ax[1].plot(x2,relative_log_error(x2,v2), label='n = 100')
ax[1].plot(x3,relative_log_error(x3,v3), label='n = 1000')
ax[1].plot(x4,relative_log_error(x4,v4), label='n = 10000')
ax[1].grid()
ax[1].set_title('Relative error')
ax[1].set_xlabel('x')
ax[1].set_ylabel('Log Error')
ax[1].legend()

fig.tight_layout()
plt.savefig('error.pdf', dpi=900)
plt.show()
