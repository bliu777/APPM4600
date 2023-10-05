import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    x0 = np.array([1, 0])
    
    Nmax = 100
    tol = 1e-10
    tol2 = 0.001
    
    t = time.time()
    for j in range(20):
      [xstar,ier,its,recalcs] =  SlackerNewton(x0,tol,tol2,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Slacker Newton: the error message reads:',ier)
    print('Slacker Newton: took this many seconds:',elapsed/20)
    print('Slacker Newton: number of iterations is:',its)
    print('Slacker Newton: numer of Jacobian recalculations is:',recalcs)
     
     
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 4*x[0]**2 + x[1]**2 - 4
    F[1] = x[0] + x[1] - math.sin(x[0] - x[1])
    return F
    
def evalJ(x): 
    
    J = np.array([[8*x[0], 2*x[1]], 
        [1 - math.cos(x[0]-x[1]), 1 + math.cos(x[0]-x[1])]])
    return J

def SlackerNewton(x0,tol,tol2,Nmax):

    ''' Slacker Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    recalcs = 0   

    for its in range(Nmax): 


       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
      
       if (norm(x1-x0) > tol2):
           J = evalJ(x0)
           Jinv = inv(J)
           recalcs += 1
 
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar,ier,its,recalcs]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its,recalcs]   

driver()
