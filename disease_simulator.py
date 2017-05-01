# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:05:03 2017

@author: Johnson, Brian, and Brendan
"""

import numpy as np
import numpy.linalg as la
import random as randy
    
lpop = 50
pop = []
stats = []

for x in range(lpop):
    pop.append(0)
    stats.append(0) 
pop = np.array([pop])
stats = np.array([stats])


def randyInfect(initInfect):
    for x in range(initInfect):
        # fix random
        infect = randy.random()
        np.put(stats, [infect], [1])
        print(stats)