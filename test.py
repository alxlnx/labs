#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
print()

print("Starting...")

plt.xlabel("x - axis")
plt.ylabel("y- axis")
plt.title("My graph")

x1 = [1, 2, 3]
y1 = [2, 4, 1]
plt.plot(x1, y1, label="line 1")

x2 = [1, 2, 3]
y2 = [4, 1, 3]
plt.plot(x2, y2, label="line 2")

x3 = [5, 6, 10, 12]
y3 = [13, 24, 64, 12]
plt.plot(x3, y3, color="green", marker = "o", markerfacecolor = "blue")

plt.legend()
plt.show()

print("Bye")