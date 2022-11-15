#!/usr/bin/python3
# This script is made for basic data processing during labs.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

T = (15.51 + 15.52) / 20
sigma_g = 0.1
sigma_L = 0.1 / 1e3
L = 599 / 1e3
sigma_T = np.sqrt(
    T*T*T * ( np.square(sigma_g) - np.square( 4 * np.square(np.pi) * sigma_L / np.square(T) ) ) / (8 * np.square(np.pi) * L)
)

sigma_t = 0.01

epsilon_g = 0.01
epsilon_L = sigma_L / L
epsilon_T = np.sqrt((np.square(epsilon_g) - np.square(epsilon_L)) / 4)
print(f'sigma_T = {epsilon_T * T}, epsilon_T = {epsilon_T * 100}%')
N0 = sigma_t / (epsilon_T* T)
print(f'N = {N0}\n')

print(f'sigma_T = {sigma_T}, epsilon_T = {(sigma_T / T) * 100}%')
N = sigma_t / sigma_T
print(f'N = {N}')
