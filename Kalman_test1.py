from filterpy.kalman import KalmanFilter
import numpy as np
from filterpy.common import Q_discrete_white_noise
import matplotlib.pyplot as plt
from kf_book.book_plots import plot_measurements
from kf_book.book_plots import plot_filter
from scipy.linalg import block_diag

class PosSensor(object):
    def __init__(self, pos = (0, 0), vel = (0, 0), noise_std = 1):
        self.vel = vel
        self.noise_std = noise_std
        self.pos = [pos[0], pos[1]]
        
    def read(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        return [self.pos[0] + np.random.randn() * self.noise_std,
                self.pos[1] + np.random.randn() * self.noise_std]


R_std = 0.35
Q_std = 0.04
def tracker1():
    tracker = KalmanFilter(dim_x = 4, dim_z = 2)
    dt = 1.0
    tracker.F = np.array([[1, dt, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, dt],
                          [0, 0, 0, 1]])
    tracker.u = 0
    tracker.H = np.array([[1/0.3048, 0, 0, 0],
                          [0, 0, 1/0.3048, 0]])
    tracker.R = np.eye(2) * R_std **2
    q = Q_discrete_white_noise(dim = 2, dt = dt ,var = Q_std ** 2)
    tracker.Q = block_diag(q, q)
    tracker.x = np.array([[0, 0, 0, 0]]).T
    tracker.P = np.eye(4) * 500
    return tracker

# Simulate robot movement
N = 30
sensor = PosSensor((0, 0), (2, 0.2), noise_std = R_std)

zs = np.array([sensor.read() for _ in range(N)])

# Run filter
robot_tracker = tracker1()
mu, cov, _, _ = robot_tracker.batch_filter(zs)

    