#!/usr/bin/python3
# This script is made for basic data processing during labs.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

T = (15.51 + 15.52) / 20
sigma_g = 0.01
sigma_L = 0.1 / 1e3
L = 665.7 / 1e3
sigma_T = np.sqrt(
    T*T*T / (8 * np.square(np.pi) * np.square(L)) *\
    ( np.square(sigma_g) - np.square( 4 * np.square(np.pi) * sigma_L / np.square(T) ) )
)

print(f'signma_T = {sigma_T}, epsilon_T = {(sigma_T / T) * 100}%')
sigma_t = 0.01
N = sigma_t / sigma_T
print(f'N = {N}')
