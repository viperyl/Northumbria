import numpy as np

def Issue(NUM):
    z_ang = []
    z_vel = [0]
    zs_ang = []
    zs_vel = []
    for i in range(NUM):
        v = np.random.randint(10)
        if np.mod(v, 2) == 0:
            for ii in range(v):
                z_vel.append(0)
        else:
            temp_vel = np.random.randint(10, size = v)
            for ii in temp_vel:
                z_vel.append(ii)
    for i in range(len(z_vel)-1):
        z_ang.append(2 * sum(z_vel[0:i+1]))
    z_ang.append(2 * z_vel[len(z_vel)-1] + z_ang[len(z_ang)-1])
    
    for i in range(len(z_vel)):
        zs_ang.append(z_ang[i]*np.random.random() + np.random.random()/10)
        zs_vel.append(z_vel[i]*np.random.random() + np.random.random())
    return z_ang, z_vel, zs_ang, zs_vel

def Issue_1(NUM):
    z_ang = []
    z_vel = [0]
    zs_ang = []
    zs_vel = []
    for i in range(NUM):
        v = np.random.randint(10)
        if np.mod(v, 2) == 0:
            for ii in range(v):
                z_vel.append(0)
        else:
            temp_vel = np.random.random(v)
            for ii in temp_vel:
                z_vel.append(ii)
            for ii in range(int((v+1)/2)):
                z_vel.append(np.random.random()*(-1)/10 - 0.2)
    z_ang = [2*(z_vel[i])+sum(z_vel[0:i]) for i in range(len(z_vel))]
    
    for i in range(len(z_vel)):
        zs_ang.append(z_ang[i]*np.random.random() + np.random.random()/10)
        zs_vel.append(z_vel[i]*np.random.random() + np.random.random()/10)
    return z_ang, z_vel, zs_ang, zs_vel
# NORMAL METHOD
def Issue_2(NUM):
    z_ang = []
    z_vel = [0]
    zs_ang = []
    zs_vel = []
    for i in range(NUM):
        v = np.random.randint(10)
        if np.mod(v, 2) == 0:
            for ii in range(v):
                z_vel.append(0)
        else:
            temp_vel = np.random.randint(10, size = v)
            for ii in temp_vel:
                z_vel.append(ii)
            for ii in range(int((v+1)/2)):
                z_vel.append(np.random.randint(8)*(-1))
    z_ang = [(z_vel[i])+sum(z_vel[0:i]) for i in range(len(z_vel))]
    
    for i in range(len(z_vel)):
        zs_ang.append(z_ang[i] + np.random.random()*10 + np.random.random()/10)
        zs_vel.append(z_vel[i] + np.random.random()*1 + np.random.random()/10)
    return z_ang, z_vel, zs_ang, zs_vel
# TESTING METHOD
def Issue_3(NUM):
    z_ang = []
    z_vel = [0]
    zs_ang = []
    zs_vel = []
    for i in range(NUM):
        v = np.random.randint(10)
        if np.mod(v, 2) == 0:
            for ii in range(v):
                z_vel.append(0)
        else:
            temp_vel = np.random.randint(10, size = v)
            for ii in temp_vel:
                z_vel.append(ii)
            for ii in range(int((v+1)/2)):
                z_vel.append(np.random.randint(8)*(-1))
    z_ang = [(z_vel[i])+sum(z_vel[0:i]) for i in range(len(z_vel))]
    
    for i in range(len(z_vel)):
        np.random.seed(123)
        if z_vel[i] == 0:
            zs_ang.append(z_ang[i] + np.random.random() + np.random.randint(14) * (np.random.random() > 0.9))
            zs_vel.append(z_vel[i] + np.random.random() + np.random.randint(8) * (np.random.random() > 0.9))
        else:
            zs_ang.append(z_ang[i] + np.random.random()*10 + np.random.random()/10 + np.random.randint(14) * (np.random.random() > 0.6))
            zs_vel.append(z_vel[i] + np.random.random()*1 + np.random.random()/10 + np.random.randint(6) * (np.random.random() > 0.9))
        
    return z_ang, z_vel, zs_ang, zs_vel

def MSE(d1, d2):
    d = np.square(d1 - d2)
    return np.sum(d)/len(d)
    