# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:08:30 2017

@author: User
"""

'''
x = 16 sin^3(t)
y = 13cos(t)-5cos(2t)-2cos(3t)-cos(4t)
'''

import matplotlib.pyplot as plt
import numpy as np

a = 1  
t = np.arange(0,2*np.pi, 0.1)
x = 16*np.sin(t)**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.plot(x,y)
#plt.savefig("heart.png",format="png",dpi=200)
plt.show()

