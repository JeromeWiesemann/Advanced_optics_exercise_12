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
tau = 20e-15

e = 1.6e-19 # C
E = 1e6 # V/m

def v(k_tilde):
    global h_bar
    global a
    global B
    global E
    global e
    # print("Frequency: " + "{:e}".format(a * e * E / (h_bar * 2 * np.pi)))
    return (B * a / h_bar) * np.sin(a * k_tilde / h_bar)

def model(y, t):
    ### Constants


    global h_bar
    global a
    global B
    global tau
    global E
    global e

    ### Model

    k_tilde = y

    dydt = e * E - m_e * B * a * np.sin(k_tilde * a / h_bar) / (tau * h_bar)
    # dydt = np.sin(k_tilde)
    return dydt



print(m_e * B * a / (tau * h_bar * e))


y_0 = [0.1]

t = np.linspace(0, 10, 2000000)

sol = odeint(model, y_0, t)


# plt.plot(t, sol[:, 0], label = "N1")
plt.plot(t, sol[:, 0], label = "N1")

plt.ylabel("Normalized population")
plt.xlabel(r"Time $[\si{\micro\s}]$")

plt.legend()
# plt.savefig("Populations_continuous.pdf", dpi = 300)
plt.show()