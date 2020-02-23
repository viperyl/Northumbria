from filterpy.kalman import KalmanFilter
import numpy as np
from filterpy.common import Q_discrete_white_noise
import matplotlib.pyplot as plt
import TEMP as tm

dt = 1
kf = KalmanFilter(dim_x = 2, dim_z = 2, dim_u = 1)
kf.P = np.array([[1, 0],
                 [0, 1]])
kf.R = 0.5
kf.Q = np.array([[0.001, 0],
                 [0, .0003]])
kf.F = np.array([[1, -1*dt],
                 [0, 1]])
kf.B = np.array([[dt],
                 [0]])
kf.H = np.array([[1, 0],
                 [0, 1]])
    
 
z_ang, z_vel, zs_ang, zs_vel = tm.Issue_3(100)
zs = []
z = []

for i in range(len(z_ang)):
    zs.append([zs_ang[i], 0.5])
    z.append([z_ang[i], 0.5])

ut = np.array(z_vel).reshape(-1,1)
zs = np.array(zs)
z = np.array(z)
result = []
for i in range(len(zs)):
    kf.predict(u =ut[i])
    kf.update(zs[i].reshape(-1,1))
    result.append(kf.x[0])
Restul = np.array([t[0] for t in result])
Actual = np.array([t[0] for t in z])
Measurements = np.array(zs_ang)
Time_seq = np.linspace(1, len(result),len(result))

line1, = plt.plot(Time_seq, Restul, label='Kalman')
line2, = plt.plot(Time_seq, Actual, label='Real')
line3, = plt.plot(Time_seq, Measurements, label='Measurements')
plt.legend()


A_R = tm.MSE(Actual, Restul)
A_M = tm.MSE(Actual, Measurements)
M_R = tm.MSE(Restul, Measurements)

ax = plt.gca()
textstr = '\n'.join((
    r'$A-R=%.2f$' % (A_R, ),
    r'$A-M=%.2f$' % (A_M, ),
    r'$M-R=%.2f$' % (M_R, )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.90, 0.10, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.show()




#plt.plot(Time_seq, Restul, Time_seq, Actual, Time_seq, Measurements)
#plt.legend()

