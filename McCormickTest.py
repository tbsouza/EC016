# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 09:27:24 2017

@author: edielson
"""

"""
Edited on Sat Nov 10 2017

@author: tbsouza
"""

#McCormick Function Problem

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from genetic_algorithm.ga_numeric import genetic_algorithm
from McCormickExample import McCormick
import matplotlib.pyplot as plt


NumIndividuals = 5
MinX1 = -5
MaxX1 = 5
MinX2 = -5
MaxX2 = 5
IndividualSize = 16
MutationRate = 0.02

MaxGeneration = 10
Target = 0.0000000001
Elitism = True


problem = McCormick(MinX1, MaxX1, MinX2, MaxX2, IndividualSize)

ClassHandle  = genetic_algorithm(problem,MutationRate,Elitism)
fit,generation = ClassHandle.search(NumIndividuals, MaxGeneration, Target)

interaction=[i for i in range(generation)]
plt.plot(interaction,fit)
plt.show()  
