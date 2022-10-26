# from cProfile import label
# from textwrap import wrap
from matplotlib import pyplot as plt  # Graphing
# import matplotlib as mpl
import numpy as np  
# import pandas as pd

figure, axes = plt.subplots(figsize=(6, 6), dpi=200)

axes.minorticks_on()
axes.grid(which='major', linestyle='--', linewidth=0.5) # '-', '--', '-.', ':', '',

font = {'fontname': 'DejaVu Serif'}
axes.set_ylabel('$Ω, с^{-1}$', **font)
axes.set_xlabel('M, кг', **font)
axes.set_title('Рис 1. Зависимость угловой скорости прецесии гироскопа от массы груза', wrap=True, **font)

# Data setup
l = 121   / 1e3
m = 1617  / 1e3
R = 39.05 / 1e3

N = 10
T0_times = np.array([32.0, 32.06, 32.13])
T_cyl_times = np.array([40.56, 40.38, 40.56])

T_cyl = np.mean(T_cyl_times) / N
T0 = np.mean(T0_times) / N

I_cyl = 0.5 * m * np.square(R)
I0 = I_cyl * np.square(T0 / T_cyl)
# print(T0 / T_cyl, np.square(T0 / T_cyl))

# НЕ учтено время реакции (0.24 * 2)
# Если просто присвоить T0_err и T_cyl_err 0.24 * 2, то отн. погр. будут 12% и 15%
# Если ещё разделить на корень из 10 (как погр. среднего), то 7% и 9%?, 
# тогда у момента инерции ротора 22% процента
T0_err =  np.std(T0_times / N, ddof=1) / np.sqrt(len(T0_times))
T_cyl_err =  np.std(T_cyl_times / N, ddof=1) / np.sqrt(len(T_cyl_times))

PR = 6
print(f'Средний период цилиндра: {T_cyl:.{PR}f}, ротора: {T0:.{PR}f}')
print(f'Момент инерции цилиндра: {I_cyl:.{PR}E}, ротора: {I0:.{PR}E}')
print(f'Среднеквадратичная ошибка СРЕДНЕГО периода цилиндра: {T_cyl_err:.{PR}f}, ротора: {T0_err:.{PR}f}')
e_cyl = (T_cyl_err / T_cyl) * 100
e0 = (T0_err / T0) * 100
print(f'Относительная ошибка СРЕДНЕГО периода цилиндра: {e_cyl:.{PR}f}%, ротора: {e0:.{PR}f}%')

σm = 0.1 / (2 * 1e3)
σR = 0.05 / 1e3
σT0 = T0_err
σT1 = T_cyl_err
T1 = T_cyl
σI0 = np.sqrt( 
      np.square( σm * (R * R * T0 * T0 / (2 * T1 * T1)) ) + \
      np.square( σR * (m * R * T0 * T0 / (T1 * T1) ) ) + \
      np.square( σT0 * ( m * R * R * T0 / (T1 * T1) ) ) + \
      np.square( σT1 * ( m * R * R * T0 * T0 / (T1 * T1 * T1) ) )
)
print(f'Ошибка момента инерции ротора: {σI0:.{PR}E}')
ε0 = (σI0 / I0) * 100
print(f'Относительная ошибка момента инерции ротора: {ε0:.{PR}f}%')

# Α α Β β Γ γ Δ δ Ε ε Ζ ζ Η η Θ θ Ι ι Κ κ Λ λ Μ μ Ν ν Ξ ξ Ο ο Π π Ρ ρ Σ σ Τ τ Υ υ Φ φ Χ χ Ψ ψ Ω ω
msrmnts = [{'M': 341 / 1e3, 't': 79, 'N': 3},
           {'M': 219 / 1e3, 't': 123.68, 'N': 3},
           {'M': 142 / 1e3, 't': 190.91, 'N': 3},
           {'M': 273 / 1e3, 't': 99, 'N': 3},
           {'M': 180 / 1e3, 't': 150.46, 'N': 3},
           {'M': 116 / 1e3, 't': 155.03, 'N': 2}
           ]
omegas = []
Ms = []
for dict in msrmnts:
  m, t, n = dict['M'], dict['t'], dict['N']
  Ms.append(m)
  T = t / n
  omega = 2 * np.pi / T
  omegas.append(omega)

print(f'Угловые скорости прецесии: ')
[print(f'{omega:.{PR}e}') for omega in omegas]

# Оценка погрешности Ω
print(f'Ошибки скорости прецессии: ')
σomegas = []
εomegas = []
σt = 0.24 * 2
for dict in msrmnts:
  t, n = dict['t'], dict['N']
  σΩ = σt * 2 * np.pi * n / (t * t)
  σomegas.append(σΩ)

for σ, omega in zip(σomegas, omegas):
  εomega = (σ / omega) * 100
  εomegas.append(εomega)

[print(f'{σomega:.{PR}e} {εomega:.{PR}f}%') for σomega, εomega in zip(σomegas, εomegas)]

σOmega = np.mean(σomegas)
print(f'Средняя ошибка Ω: {σOmega:.{PR}E}')
axes.errorbar(Ms, omegas, xerr=σm, yerr=σOmega, 
              lw=0,
              capsize=1.5, elinewidth=1.5,
              fmt='ok',
              ms=3, 
              label='$Ω(M)$')
(k, b) = np.polyfit(Ms, omegas, 1)
x = np.linspace(0.116, 0.341, 10)
axes.plot(x, k * x + b, '-r', linewidth=1, label=f'Линейная аппроксимация $Ω = {k:.4f}M {b:.4f}$')

g = 9.815
νs = []
ωs = []
for m, Ω in zip(Ms, omegas):
  ω0 = m * g * l / (I0 * Ω)
  ωs.append(ω0)
  T0 = 2 * np.pi / ω0
  ν0 = 1 / T0
  νs.append(ν0)

ν0 = np.mean(νs)
ω0 = np.mean(ωs)
print(f'Средняя частота вращения ротора гироскопа: {ν0:.{PR}f}Гц')

σω0s = []
for σomega, omega in zip(σomegas, omegas):
  σω0 = np.sqrt(
        np.square( σm * g * l / (I0 * omega)) + \
        np.square( σI0 * m * g * l / (omega * I0 * I0) ) + \
        np.square( σomega * m * g * l / (I0 * omega * omega) )
        )
  σω0s.append(σω0)

σω0 = np.mean(σω0s) 
σν0 = σω0 / (np.pi * 2)
print(f'Ошибка частоты вращения ротора гироскопа: {σν0:.{PR}f}')
print(f'Относительная ошибка частоты вращения ротора гироскопа: {(σν0 / ν0 * 100):.{PR}f}%')

h = (16 - 15.25) / 1e2
tтр = 29
Mтр = 0.5 * I0 * ω0 * h / (l * tтр) 
print(f'Момент инерции силы трения: {Mтр:.{PR}e}')

LΩ = 0.5 * I0 * max(omegas)
Lω = I0 * ω0
print(f'LΩ: {LΩ:.{PR}f}, Lω: {Lω:.{PR}f}')

# ------
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
# plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)
# plt.ylabel("$u=T^2 a$, $с^2 \cdot м$")  # подписи к осям
axes.legend(fontsize=8)
figure.savefig('omega(M).png')
plt.show()
