'''
Created on Jan 12, 2018

@author: sjl
'''
import numpy as np
from numpy.polynomial.tests.test_classes import random
def getPlusOper(nums=10):
    element=[]
    labs=[]
    for i in range(nums):
        element.append([i,i])
        labs.append([i+i])
    return(element,labs)
def getRandomPlusOper(num=10):
    element=[]
    labs=[]
    for i in range(num):
        va=np.random.randint(100,size=2)
        element.append(va)
        labs.append([va[0]+va[1]])
    return (element,labs)
def getMulOper(nums=10):
    element=[]
    labs=[]
    for i in range(nums):
        element.append([i,i])
        labs.append([i*i])

    return(element,labs)
def getRandomMulOper(num=10):
    element=[]
    labs=[]
    for i in range(num):
        va=np.random.randint(100,size=2)
        element.append(va)
        labs.append([va[0]*va[1]])
    return (element,labs)
