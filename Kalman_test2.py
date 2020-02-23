from filterpy.kalman import KalmanFilter
import numpy as np
from filterpy.common import Q_discrete_white_noise
import matplotlib.pyplot as plt
from kf_book.book_plots import plot_measurements
from kf_book.book_plots import plot_filter
from scipy.linalg import block_diag

dt = 1.0
R = 3
kf = KalmanFilter(dim_x = 2, dim_z = 1, dim_u = 1)
kf.P *= 10
kf.R *= R
kf.Q  = Q_discrete_white_noise(2, dt, 0.1)
kf.F = np.array([[1, 0],
                 [0, 1]])
kf.B = np.array([[dt],
                 [1]])
kf.H = np.array([[1, 0]])

zs = [i + np.random.randn() * R for i in range(1, 1000)]
xs = []
cmd_velocity = 1

for z in zs:
    kf.predict(u = cmd_velocity)
    kf.update(z)
    kf.append(kf.x[0])
    
