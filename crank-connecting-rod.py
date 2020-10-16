# -*- coding: utf-8 -*-
"""
crank-connecting rod mechanism
Author: Ferhat Kurtulmuş
"""

import numpy as np
import pylab as pl

from sympy import Eq, cos, sin, solve, symbols

w1 = 1 # crank's angular velocity
crankLen = 0.5
rodLen = 0.7

positions = []
velocities = []

for _ka in np.linspace(0, 360, 20):
    ka = np.radians(_ka)
    
    # analyze position of the piston
    teta, s = symbols('teta, s')
    eq1 = Eq(crankLen*cos(ka) + rodLen*cos(teta)-s)
    eq2 = Eq(crankLen*sin(ka) + rodLen*sin(teta))
    
    res = solve((eq1, eq2), (teta, s))
    
    sval = res[0][1]
    tetaval =  res[0][0]
    
    # analyze velocity of the piston using derivative of the position eqs
    # w2 is angular velocity of the rod
    w2, V = symbols('w2, V')
    eq11 = Eq(-crankLen*np.sin(ka)*w1 - rodLen*sin(tetaval)*w2-V)
    eq22 = Eq(crankLen*np.cos(ka)*w1 + rodLen*cos(tetaval)*w2)
    reshiz = solve((eq11, eq22), (w2, V))
    
    positions.append(sval)
    velocities.append(reshiz[V])

pl.figure(); pl.plot(np.linspace(0, 360, 20), positions); pl.title('Piston positions')
pl.figure(); pl.plot(np.linspace(0, 360, 20), velocities); pl.title('Piston velocities')