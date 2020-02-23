from filterpy.kalman import KalmanFilter
import numpy as np
from filterpy.common import Q_discrete_white_noise
import matplotlib.pyplot as plt
from kf_book.book_plots import plot_measurements
from kf_book.book_plots import plot_filter
from scipy.linalg import block_diag
import TEMP as tm


dt = 2
kf = KalmanFilter(dim_x = 2, dim_z = 2, dim_u = 1)
kf.P = np.array([[1, 0],
                 [0, 1]])
kf.R = 0.05
kf.Q = np.array([[0.001, 0],
                 [0, 0.003]])
kf.F = np.array([[1, -1*dt],
                 [0, 1]])
kf.B = np.array([[dt],
                 [0]])
kf.H = np.array([[1, 0],
                 [0, 1]])
    
    
z_ang, z_vel, zs_ang, zs_vel = tm.Issue_1(50)
zs = []
z = []

for i in range(len(z_ang)):
    zs.append([zs_ang[i], 0.01])
    z.append([z_ang[i], 0.01])

ut = np.array(z_vel).reshape(-1,1)
zs = np.array(zs)
z = np.array(z)
result = []
for i in range(len(zs)):
    kf.predict(u =ut[i])
    kf.update(zs[i].reshape(-1,1))
    result.append(kf.x[0])
Restul = [t[0] for t in result]
Actual = [t[0] for t in z]
Time_seq = np.linspace(1, len(result),len(result))



plt.plot(Time_seq, Restul, Time_seq, Actual)



