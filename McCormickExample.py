'''
Created on 21 de set de 2016

@author: edielson
'''


"""
Edited on Sat Nov 10 2017

@author: tbsouza
"""


import numpy as np
import math

class McCormick(object):
    '''
    classdocs
    '''

    def __init__(self, x1_min,x1_max,x2_min,x2_max,individual_size):
        '''
        Constructor
        '''
        self.x1_min = x1_min
        self.x1_max = x1_max
        self.x2_min = x2_min
        self.x2_max = x2_max
        self.individual_size = individual_size
        self.max_symbol = 1
        self.min_symbol = 0
        
#    Rosembrock Functiom
#    def Rosembrock_Function(self, x1,x2):
#        return (1.0-x1)**2 + 100.0*(x2-x1**2)**2
#    
    
#    Eggholder Function
#    def Rosembrock_Function(self, x1,x2):
#        x = x1
#        y = x2
#        
#        a = (-(y+47))*(math.sin(math.sqrt(math.fabs((x/2)+(y+47)))))
#        b = x*(math.sin(math.sqrt(math.fabs(x - (y+47)))))
#        
#        return (a - b)
    
    
##################################################################################   
#    McCormick Function
    def McCormick_Function(self, x1,x2):
        x = x1
        y = x2
        
        return (2*(x**2)) - (1.05*(x**4)) + ((x**6)/6.0) + (x*y) + (y**2)
    
##################################################################################    
    

    def x1Real(self, x1Decimal):
        Precision = (self.x1_max - self.x1_min)/((2.0**(self.individual_size/2)) - 1)
        #print('Precision x1 = %g' %Precision)
        return self.x1_min+Precision*x1Decimal
    
    def x2Real(self, x2Decimal):
        Precision = (self.x2_max - self.x2_min)/((2.0**(self.individual_size/2)) - 1)
        #print('Precision x2 = %g' %Precision)
        return self.x2_min+Precision*x2Decimal
        
    def initPopulation(self, num_individuals):
        
        num_individuals
        
        population = []
        #Cria todos os indiviudos e insere na populacao inicial
        for i in range(num_individuals):
            individual = np.random.binomial(1,0.5,self.individual_size)
            print(individual)
            population.append(individual.tolist())
        return population    
    
    def bin_to_dec(self,bin_x):
        s=''.join(str(x) for x in bin_x)
        return(int(s,2))
               
    def fitness(self,population):
    
        fitnessPop=[]
        #calculate the fitness for each individual of population
        for individual in population:
            fitnessPop.append(self.getFitness(individual))
    
        return fitnessPop
    
    def getIndividualSize(self):
        return self.individual_size
    
    def getMaxGeneSymbol(self):
        return self.max_symbol
    
    def getMinGeneSymbol(self):
        return self.min_symbol
    
    
    def getFitness(self,individual):
        
        dec_ind_x1 = self.bin_to_dec(individual[:self.individual_size/2])
        dec_ind_x2 = self.bin_to_dec(individual[self.individual_size/2:])
        real_x1 = self.x1Real(dec_ind_x1)
        real_x2 = self.x2Real(dec_ind_x2)
        #print(self.McCormick_Function(real_x1,real_x2))
        fitness = 10.0/(1.0+self.McCormick_Function(real_x1,real_x2))
        #print(fitness)
        return fitness
    
    def printSolution(self,solution):
        
        print('Solution:')
        print(solution)
        dec_ind_x1 = self.bin_to_dec(solution[:self.individual_size/2])
        dec_ind_x2 = self.bin_to_dec(solution[self.individual_size/2:])
        #print(dec_ind_x1)
        #print(dec_ind_x2)
        real_x1 = self.x1Real(dec_ind_x1)
        real_x2 = self.x2Real(dec_ind_x2)
        print('x1=%g'%real_x1)
        print('x2=%g'%real_x2)
        print('f(x1,x2)=%g'%self.McCormick_Function(real_x1,real_x2))