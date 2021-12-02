# %%

import matplotlib.pyplot as plt

B = 14 # T
l = 0.2 # m
a = 1 # H/m
L0 = 8 # H
m = 0.1  # kg
R = 3 # Ohm
E = 1 # V

XMAX = 10

dt = 0.001 # s
x0 = 0 # m
v0 = 0 # m/s
vd0 = 0 # m/s^2
vdd0 = E*l*B/(m*L0) # m/s^3

# %%

T = [0]
X = [x0]
V = [v0]
VD = [vd0]
VDD = [vdd0]
VDDD = []
L = [L0]

A1 = B*l
A02 = a*m/A1
A3 = m/A1
A2 = m*R/A1

while X[-1]< XMAX:
    VDDD.append((-A1*VD[-1]-A02*V[-1]*VDD[-1]-A2*VDD[-1])/(A3*L[-1]))
    L.append(L[-1]+a*V[-1]*dt)
    X.append(X[-1]+V[-1]*dt)
    V.append(V[-1]+VD[-1]*dt)
    VD.append(VD[-1]+VDD[-1]*dt)
    VDD.append(VDD[-1]+VDDD[-1]*dt)
    T.append(T[-1]+dt)


# %%

plt.plot(T, X, label="$x$ (m)")
# plt.plot(T, L, label="$L$ (H)")
plt.plot(T, V, label="$v$ (m/s)")
plt.plot(T, VD, label="$a$ (m/s$^2$)")
plt.plot(T, VDD, label="$j$ (m/s$^3$)")
plt.plot(T[:-1], VDDD, label="$s$ (m/s$^4$)")
plt.grid()
plt.legend()
plt.show()