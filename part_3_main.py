import numpy as np
import matplotlib.pyplot as plt
from euler_rocket import *


x=0
y=0
dt=0.0001
v0=690
theta0=50
friction=0.0003348



def kassam_in_air (dt , x_0 , y_0 , vx_0 , vy_0, friction_coefficient):
    x_n = x_0
    y_n = y_0
    vx_n = vx_0
    vy_n = vy_0
    x = []
    y = []
    while y_n > 10 ** (-9) or len(y)<2:
        x.append(x_n)
        y.append(y_n)
        x_n, y_n, vx_n, vy_n = part_three_rocket_iteration(x_n, y_n, vx_n, vy_n, dt, friction_coefficient)
    return x, y


if __name__ == '__main__':
    v_x0 = v0*np.cos(theta0*np.pi / 180.)
    v_y0 = v0*np.sin(theta0*np.pi / 180.)

    x,y = kassam_in_air(dt,x,y,v_x0,v_y0, friction)

    t_array = np.array([n * dt for n in range(len(x))])
    x_array = np.array(x)
    y_array = np.array(y)
    plt.plot(x_array, y_array)
    plt.xlabel(r'$x$ [$\mathrm{m}$]', size=15)
    plt.ylabel(r'$y$ [$\mathrm{m}$]', size=15)
    plt.title('Part 3 - Rocket launch in vacuum')
    plt.grid()
    plt.show()
    print(x[-1])