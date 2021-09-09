using PyPlot

plt.style.use("seaborn-paper")

PyPlot.rc("font", family="serif")
PyPlot.rc("text", usetex=true)
PyPlot.matplotlib.rcParams["axes.titlesize"] = 10
PyPlot.matplotlib.rcParams["axes.labelsize"] = 10
PyPlot.matplotlib.rcParams["xtick.labelsize"] = 9
PyPlot.matplotlib.rcParams["ytick.labelsize"] = 9

const sw = 3.40457
const dw = 7.05826

x = -3pi:pi/1000:+3pi
y = sin.(x)./x
z = tanh.(x)./x

fig, axs = plt.subplots(2,1, figsize=(sw,dw), sharex=true, sharey=true, constrained_layout=true)
axs[1].plot(x, y, "-C0")
axs[2].plot(x, z, "--C1")
axs[2].set_xlabel("\$ x \$")
plt.savefig("./julia_example.pdf", bbox_inches="tight")
plt.close()

