from filterpy.kalman import KalmanFilter
import numpy as np
from filterpy.common import Q_discrete_white_noise
import matplotlib.pyplot as plt
from kf_book.book_plots import plot_measurements
from kf_book.book_plots import plot_filter
from scipy.linalg import block_diag

def tracker1():
    tracker = KalmanFilter(dim_x = 2, dim_z = 2)
    dt = 0.002
    tracker.F = np.array([[1, -1 * dt],
                          [0, 1]])
    
    tracker.u = 0.0
    
    tracker.H = np.array([[1, 0]])
    
    tracker.R = 0.05
    q = Q_discrete_white_noise(dim = 2, dt = dt, var = 0.01)
    
    tracker.Q = q
    tracker.x = np.array([[0, 0]]).T
    tracker.P = np.eye(2) * 5
    return tracker

z_ang, z_vel, zs_ang, zs_vel = tm.Issue(50)
zs = []
z = []

for i in range(len(z_ang)):
    zs.append([zs_ang[i], 0.5])
    z.append([z_ang[i], 0.5])

ut = np.array(z_vel).reshape(-1,1)
zs = np.array(zs)
z = np.array(z)
result = []

tilt_tracker = tracker1()
mu,cov, tan, tve = tilt_tracker.batch_filter(zs,ut)
Time = np.linspace(1, len(zs), len(zs))
plot_measurements(Time, zs[:,1])







x = np.array([[0, 0]]).T
P = np.diag([10.0, 10.0])
dt = 0.005
F = np.array([[1, -1*dt], 
              [0, 1]])
Q = Q_discrete_white_noise(dim = 2, dt = 1, var = 2.35)
B = np.array([[dt, 0]]).T
H = np.array([[1.0, 0.0]])
R = 0.5
I = np.array([[1, 0],
              [0, 1]])
    
z_ang, z_vel, zs_ang, zs_vel = tm.Issue(50)
zs = []
z = []

for i in range(len(z_ang)):
    zs.append([zs_ang[i], 0.5])
    z.append([z_ang[i], 0.5])

ut = np.array(z_vel).reshape(-1,1)
zs = np.array(zs)
z = np.array(z)
result = []
for i in range(len(z)):
    result.append(KM_YX(zs[0].reshape(-1,1), zs_vel[i], P))








