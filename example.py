import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc

plt.style.use('seaborn-paper')

rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)
matplotlib.rcParams['axes.titlesize'] = 10
matplotlib.rcParams['axes.labelsize'] = 10
matplotlib.rcParams['xtick.labelsize'] = 9
matplotlib.rcParams['ytick.labelsize'] = 9

sw = 3.40457
dw = 7.05826

x = np.arange(-3*np.pi, +3*np.pi, np.pi/1000)
y = np.sin(x)/x
z = np.tanh(x)/x

fig, axs = plt.subplots(2,1, figsize=(sw,dw), sharex=True, sharey=True, constrained_layout=True)
axs[0].plot(x, y, "-C0")
axs[1].plot(x, z, "--C1")
axs[1].set_xlabel(r"$ x $")
plt.savefig("./python_example.pdf", bbox_inches="tight")
plt.close()

