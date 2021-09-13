import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib


matplotlib.rcParams.update({'font.size':14})

df = pd.read_csv('data_with_10_xes.txt', sep=' ', header=None)
u1 = df[1].to_numpy()

df = pd.read_csv('data_with_100_xes.txt', sep=' ', header=None)
u2 = df[1].to_numpy()

df = pd.read_csv('data_with_1000_xes.txt', sep=' ', header=None)
u3 = df[1].to_numpy()

df = pd.read_csv('data_with_10000_xes.txt', sep=' ', header=None)
u4 = df[1].to_numpy()

df = pd.read_csv('approx_with_10_xes.txt', sep=' ', header=None)
x1 = np.flip(df[0].to_numpy())
v1 = np.flip(df[1].to_numpy())

df = pd.read_csv('approx_with_100_xes.txt', sep=' ', header=None)
x2 = np.flip(df[0].to_numpy())
v2 = np.flip(df[1].to_numpy())

df = pd.read_csv('approx_with_1000_xes.txt', sep=' ', header=None)
x3 = np.flip(df[0].to_numpy())
v3 = np.flip(df[1].to_numpy())

df = pd.read_csv('approx_with_10000_xes.txt', sep=' ', header=None)
x4 = np.flip(df[0].to_numpy())
v4 = np.flip(df[1].to_numpy())

fig, ax = plt.subplots(2,2, figsize=(14,8))

plt.suptitle('Poisson equation', fontsize=18)
plt.subplots_adjust(top=0.9)

ax[0][0].plot(x1,u1)
ax[0][0].plot(x1,v1)
ax[0][0].grid()
ax[0][0].set_xlabel('x')
ax[0][0].set_ylabel('u(x)')
ax[0][0].legend(['Real solution', 'Approximated solution \n with 10 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

ax[0][1].plot(x2,u2)
ax[0][1].plot(x2,v2)
ax[0][1].grid()
ax[0][1].set_xlabel('x')
ax[0][1].set_ylabel('u(x)')
ax[0][1].legend(['Real solution', 'Approximated solution \n with 100 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

ax[1][0].plot(x3,u3)
ax[1][0].plot(x3,v3)
ax[1][0].grid()
ax[1][0].set_xlabel('x')
ax[1][0].set_ylabel('u(x)')
ax[1][0].legend(['Real solution', 'Approximated solution \n with 1000 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)

ax[1][1].plot(x4,u4)
ax[1][1].plot(x4,v4)
ax[1][1].grid()
ax[1][1].set_xlabel('x')
ax[1][1].set_ylabel('u(x)')
ax[1][1].legend(['Real solution', 'Approximated solution \n with 10000 points'] ,bbox_to_anchor = (0.57, 1), fontsize=12)


plt.savefig('poisson.pdf', dpi=900)
plt.show()


#Task 8a
def absolute_log_error(u, v):
    abs_error = []
    for i in range(len(u)):
        abs_error.append(np.log10(abs(u[i]-v[i])))
    return abs_error

#Task 8b
def relative_log_error(u, v):
    rel_error = []
    for i in range(len(u)):
        rel_error.append(np.log10(abs((u[i]-v[i])/u[i])))
    return rel_error


fig, ax = plt.subplots(2,1, figsize=(12,8))

plt.subplots_adjust(top=0.9)

ax[0].plot(x1,absolute_log_error(u1,v1), label='n = 10')
ax[0].plot(x2,absolute_log_error(u2,v2), label='n = 100')
ax[0].plot(x3,absolute_log_error(u3,v3), label='n = 1000')
ax[0].plot(x4,absolute_log_error(u4,v4), label='n = 10000')
ax[0].grid()
ax[0].set_title('Absolute error')
ax[0].set_xlabel('x')
ax[0].set_ylabel('Log Error')
ax[0].legend()


ax[1].plot(x1,relative_log_error(u1,v1), label='n = 10')
ax[1].plot(x2,relative_log_error(u2,v2), label='n = 100')
ax[1].plot(x3,relative_log_error(u3,v3), label='n = 1000')
ax[1].plot(x4,relative_log_error(u4,v4), label='n = 10000')
ax[1].grid()
ax[1].set_title('Relative error')
ax[1].set_xlabel('x')
ax[1].set_ylabel('Log Error')
ax[1].legend()

fig.tight_layout()
plt.savefig('error.pdf', dpi=900)
plt.show()



#Problem 10 plots

df = pd.read_csv('time10n.txt', sep=' ', header=None)
gen10 = df[0].to_numpy()
spe10 = df[1].to_numpy()
mean10 = [np.mean(gen10),np.mean(spe10)]

df = pd.read_csv('time100n.txt', sep=' ', header=None)
gen100 = df[0].to_numpy()
spe100 = df[1].to_numpy()
mean100 = [np.mean(gen100),np.mean(spe100)]

df = pd.read_csv('time1000n.txt', sep=' ', header=None)
gen1000 = df[0].to_numpy()
spe1000 = df[1].to_numpy()
mean1000 = [np.mean(gen1000),np.mean(spe1000)]

df = pd.read_csv('time10000n.txt', sep=' ', header=None)
gen10000 = df[0].to_numpy()
spe10000 = df[1].to_numpy()
mean10000 = [np.mean(gen10000),np.mean(spe10000)]

df = pd.read_csv('time100000n.txt', sep=' ', header=None)
gen100000 = df[0].to_numpy()
spe100000 = df[1].to_numpy()
mean100000 = [np.mean(gen100000),np.mean(spe100000)]


it = np.linspace(0,50, 50)

def plotting_times(gen,spe, n):
    ratio = gen/spe
    coef = np.polyfit(it,ratio,1)
    poly1d_fn = np.poly1d(coef)
    fig,ax = plt.subplots(2,1,figsize=(14,8))

    plt.suptitle('Run times for general and special solution with n ='+str(n))

    ax[0].plot(it,gen, label='General solution')
    ax[0].plot(it,spe, label='Special solution')
    ax[0].set_xlabel('Run number')
    ax[0].set_ylabel('Time [s]')
    ax[0].legend()

    ax[1].plot(it,gen/spe,'-b',label='Ratio')
    ax[1].plot(it,poly1d_fn(it),'--r',label='Linear fit, mean ratio = '+str(np.round(np.mean(gen/spe),3)))
    ax[1].set_xlabel('Run number')
    ax[1].set_ylabel('General/Special')
    ax[1].legend()

    plt.savefig('time'+str(n)+'.pdf', dpi=900)
    plt.show()

plotting_times(gen10,spe10,10)
plotting_times(gen100,spe100,100)
plotting_times(gen1000,spe1000,1000)
plotting_times(gen10000,spe10000,10000)
plotting_times(gen100000,spe100000,100000)
