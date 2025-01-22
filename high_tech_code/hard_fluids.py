import numpy as np 
from scipy.integrate import odeint 

def ode(x,t):
    return [x[1], -x[0]]

def get_ode_solns():
    t = np.linspace(0, 10, 100)
    x0 = [1, 0]
    x = odeint(ode, x0, t)
    return t, x