import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import odeint

plt.rcParams["text.usetex"] = True
plt.rc('text.latex', preamble=r'\usepackage{siunitx}')

# h_bar = 6.62e-34 / (2 * np.pi)
h_bar = 1.054571817e-34 # J * s
a = 5e-10 # m
B = 3*1.6e-19 # J
m_e = 9.10e-31 # kg
tau = 20e-15 # 1/s

e = 1.6e-19 # C
E = 10e6 # V/m

def v(k_tilde):
    global h_bar
    global a
    global B
    global E
    global e
    # print("Frequency: " + "{:e}".format(a * e * E / (h_bar * 2 * np.pi)))
    return B * a * np.sin(k_tilde * a * e * E / h_bar) / h_bar


def model(y, t):
    ### Constants


    global h_bar
    global a
    global B
    global tau
    global E
    global e

    ### Model

    k_tilde, x = y

    dydt = [1 - m_e * B * a * np.sin(k_tilde * a * e * E / h_bar) / (tau * h_bar * e * E), B * a * np.sin(k_tilde * a * e * E / h_bar) / (h_bar)]
    # dydt = 1 - 64.71820970349333 * np.sin(k_tilde * a * e * E / h_bar)
    # dydt = np.sin(k_tilde)
    return dydt



print(a * e * E / h_bar)


y_0 = [0, 0]

t = np.linspace(0, 1e-11, 2000000)

sol = odeint(model, y_0, t)




tau = 20e-10 # 1/s
sol = odeint(model, y_0, t)
plt.plot(t, sol[:, 1], label = r"$\tau = 20\cdot 10^{-10}$")

tau = 20e-14 # 1/s
sol = odeint(model, y_0, t)
plt.plot(t, sol[:, 1], label = r"$\tau = 20\cdot 10^{-14}$")

tau = 20e-15 # 1/s
# plt.plot(t, sol[:, 0], label = "N1")
# plt.plot(t, v(sol[:, 0]), label = "N1")
sol = odeint(model, y_0, t)
plt.plot(t, sol[:, 1], label = r"$\tau = 20\cdot 10^{-15}$")


plt.ylabel(r"Position $x\,[\si{\m}]$")
plt.xlabel(r"Time $[\si{\s}]$")

plt.legend()
plt.savefig("Position_over_time_multiple_tau.pdf", dpi = 300)
plt.show()