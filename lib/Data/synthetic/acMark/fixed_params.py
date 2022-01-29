import numpy as np

z = 12
n = 2 ** z
m = 2 ** (z + 5)
max_deg = 500
k = 6
d = 100

M = np.array([
    [0.6, 0.08, 0.08, 0.08, 0.08, 0.08],
    [0.08, 0.6, 0.08, 0.08, 0.08, 0.08],
    [0.08, 0.08, 0.6, 0.08, 0.08, 0.08],
    [0.08, 0.08, 0.08, 0.6, 0.08, 0.08],
    [0.08, 0.08, 0.08, 0.08, 0.6, 0.08],
    [0.08, 0.08, 0.08, 0.08, 0.08, 0.6]
])

D = np.array([
    [0.2, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.2, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.25, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.25, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.3, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.3]
])