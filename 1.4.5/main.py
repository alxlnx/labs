#!/usr/bin/python3
from matplotlib import pyplot as plt  # Graphing
import numpy as np  
figure, axes = plt.subplots(figsize=(6, 6), dpi=200)

import numpy as np


def lin_ls(x, y, through_null=False):
    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        if len(x) != len(y):
            raise ValueError("Incompatible x and y vectors. They must have the same length.")
        if through_null:
            k = np.mean(x * y) / np.mean(x * x)
            s_k = np.sqrt(1 / len(x)) * np.sqrt(np.mean(y * y) / np.mean(x * x) - k ** 2)
            return k, s_k
        else:
            xy = np.mean(x * y)
            x1y = np.mean(x) * np.mean(y)
            x2 = np.mean(x * x)
            x12 = np.mean(x) ** 2
            y2 = np.mean(y * y)
            y12 = np.mean(y) ** 2
            k = (xy - x1y) / (x2 - x12)
            b = np.mean(y) - k * np.mean(x)
            s_k = np.sqrt(1 / len(x)) * np.sqrt((y2 - y12) / (x2 - x12) - k ** 2)
            s_b = s_k * np.sqrt(x2 - x12)
            return k, s_k, b, s_b
    else:
        raise ValueError("Invalid x or/and y type. Must be numpy.ndarray.")


axes.minorticks_on()
axes.grid(which='major', linestyle='--', linewidth=0.5) # '-', '--', '-.', ':', '',
font = {'fontname': 'DejaVu Serif'}
axes.set_ylabel('$ν, Гц$', **font)
axes.set_xlabel('n', **font)
axes.set_title('Рис 1. Зависимость частоты от номера гармоники', wrap=True, **font)

# Data setup
L = 50 / 1e2
g = 9.815
ρl = 568.4 / (1e3 * 1e3)

ms = np.array([1039.9, 1541.3, 1978.7, 1876.5, 583.7])
ms /= 1e3
Ts = []
for m in ms:
  T = m * g
  Ts.append(T)
print(f'Силы натяжения для масс:')
print(Ts)
Ts = np.array(Ts)

freqs1 = [134.4, 274, 402.6, 555, 684, 833, 964, 1107] # [138.9, 277.8, 416.7, 555.6, 714, 833, 952.4, 1111, 1052.6]
freqs2 = [163.9, 331, 495, 662, 826, 994, 1160] #[166.6, 333, 500, 660, 833, 1000, 1111]
freqs3 = [196, 399, 589, 787.3, 889, 1182] #[200, 400, 588, 769.2, 909, 1170]
freqs4 = [195, 392, 589, 786, 981, 982] #[192.3, 384.6, 555, 833, 1000, 952]
freqs5 = [112, 192, 342, 386, 575, 580] #[100.4, 178.5, 357, 384, 555.5, 555]

ns1, ns2, ns3, ns4, ns5 = np.arange(1, len(freqs1) + 1), \
                          np.arange(1, len(freqs2) + 1), \
                          np.arange(1, len(freqs3) + 1), \
                          np.arange(1, len(freqs4) + 1), \
                          np.arange(1, len(freqs5) + 1)
PR = 1
axes.scatter(ns1, freqs1, marker='o', s = 25, color='r', label=f'T = {Ts[0]:.{PR}f}')
axes.scatter(ns2, freqs2, marker='^', s = 25, color='g', label=f'T = {Ts[1]:.{PR}f}')
axes.scatter(ns3, freqs3, marker='x', s = 25, color='b', label=f'T = {Ts[2]:.{PR}f}')
axes.scatter(ns4, freqs4, marker='s', s = 25, color='y', label=f'T = {Ts[3]:.{PR}f}')
axes.scatter(ns5, freqs5, marker='+', s = 25, color='m', label=f'T = {Ts[4]:.{PR}f}')

(k1, b1) = np.polyfit(ns1, freqs1, 1)
(k2, b2) = np.polyfit(ns2, freqs2, 1)
(k3, b3) = np.polyfit(ns3, freqs3, 1)
(k4, b4) = np.polyfit(ns4, freqs4, 1)
(k5, b5) = np.polyfit(ns5, freqs5, 1)

ng1 = np.arange(0, len(freqs1) + 2)
ng2 = np.arange(0, len(freqs2) + 2)
ng3 = np.arange(0, len(freqs3) + 2)
ng4 = np.arange(0, len(freqs4) + 2)
ng5 = np.arange(0, len(freqs5) + 2)
axes.plot(ng1, k1 * ng1 + b1, '--r', linewidth=1, label=f'Линейная аппроксимация $ ν = {k1:.1f}T + {b1:.1f}$')
axes.plot(ng2, k2 * ng2 + b2, '--g', linewidth=1, label=f'Линейная аппроксимация $ ν = {k2:.1f}T + {b2:.1f}$')
axes.plot(ng3, k3 * ng3 + b3, '--b', linewidth=1, label=f'Линейная аппроксимация $ ν = {k3:.1f}T + {b3:.1f}$')
axes.plot(ng4, k4 * ng4 + b4, '--y', linewidth=1, label=f'Линейная аппроксимация $ ν = {k4:.1f}T + {b4:.1f}$')
axes.plot(ng5, k5 * ng5 + b5, '--m', linewidth=1, label=f'Линейная аппроксимация $ ν = {k5:.1f}T + {b5:.1f}$')
axes.set_xlim(0, 10)

u1 = k1 * 2 * L
u2 = k2 * 2 * L
u3 = k3 * 2 * L
u4 = k4 * 2 * L
u5 = k5 * 2 * L
us = [u1, u2, u3, u4, u5]
#us[0] = 133.9
#us[1] = 164
#us[2] = 184.7
#us[3] = 179.9 # Искусственно более точная скорость
#us[4] = 100.1

print(f'Скорости волны: ')
print(us)
# Погрешность u:
# n = len(freqs1)
# sigma_k = np.sqrt( (1 / (n - 2)) * (np.std(freqs1) / np.std(ns1) - k1 * k1) )
# sigma_b = sigma_k * np.sqrt(np.mean(ns1 * ns1))
# print(sigma_k, sigma_b)

ussq = []
for u in us:
  ussq.append(np.square(u))
ussq = np.array(ussq)

figure2, axes2 = plt.subplots(figsize=(6, 6), dpi=200)
axes2.minorticks_on()
axes2.grid(which='major', linestyle='--', linewidth=0.5) # '-', '--', '-.', ':', '',
axes2.set_title('Рис 2. Зависимость квадрата скорости от силы натяжения', wrap=True, **font)
axes2.set_xlabel('T, H')
axes2.set_ylabel('$u^2, м^2/c^2$')
axes2.scatter(Ts, ussq, marker='o', color=[0,0,0], label=f'$u^2$ = kT')

(k_tu, b_tu) = np.polyfit(Ts, ussq, 1)
# (k_tu, s_k)= lin_ls(Ts, ussq, through_null=True)
axes2.plot(Ts, k_tu * Ts + b_tu, '--r', linewidth=1, label=f'Линейная аппроксимация $ u^2 = {k_tu:.1f}T + {b_tu:.1f}$')

# Α α Β β Γ γ Δ δ Ε ε Ζ ζ Η η Θ θ Ι ι Κ κ Λ λ Μ μ Ν ν Ξ ξ Ο ο Π π Ρ ρ Σ σ Τ τ Υ υ Φ φ Χ χ Ψ ψ Ω ω

# axes.errorbar(Ms, omegas, xerr=σm, yerr=σOmega, 
#               lw=0,
#               capsize=1.5, elinewidth=1.5,
#               fmt='ok',
#               ms=3, 
#               label='$Ω(M)$')

# ------
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
# plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)
# plt.ylabel("$u=T^2 a$, $с^2 \cdot м$")  # подписи к осям
axes.legend(fontsize=5)
axes2.legend()
figure.savefig('nu(n).png')
figure2.savefig('u_sq(T).png')
plt.show()
