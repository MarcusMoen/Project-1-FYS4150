import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.rcParams.update({'font.size':14})

df = pd.read_csv('data.txt', sep=' ', header=None)
x = df[0].to_numpy()
u = df[1].to_numpy()

plt.plot(x,u)
plt.grid()
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Poisson equation')
plt.savefig('possion1.png', dpi=900)
