# import libraries
import numpy as np
    
def driver():

# test functions 
    f1 = lambda x: (10/np.add(x,4))**(1/2)
# fixed point is alpha1 = 1.4987....
    f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 
    Nmax = 100
    tol = 10e-10
# test f1 '''
    x0 = 1.5
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f1(xstar))
    print('Error message reads:',ier)

# test aitkens
    Nmax = 98
    tol = 10e-10

    [phat,ier] = aitkens(xstar,tol,Nmax)
    print('the approximate fixed point is:',phat)
    print('f1(xstar):',f1(phat))
    print('Error message reads:',ier)
    
    
#test f2 '''
#    x0 = 0.0
#    [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
#    print('the approximate fixed point is:',xstar)
#    print('f2(xstar):',f2(xstar))
#    print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):
    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    count = 0
    xArr = []
    while (count <Nmax):
        count = count +1
        x1 = f(x0)
        xArr.append(x1)
        if (abs(x1-x0) <tol):
            xstar = x1
            xArr.append(x1)
            ier = 0
            return [xArr,ier]
        x0 = x1

    xstar = x1
    xCol = np.array(xArr, order = 'F')
    ier = 1
    return [xCol, ier]
   
 
# define routines
def aitkens(p,tol,Nmax):
    ''' p = initial appx''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    count = 0
    pArr = []
    while (count < Nmax):
        count = count + 1
        pHatn = np.subtract(p[count], ((p[count + 1] - p[count]) ** 2) / (p[count+ 2] - 2 * p[count + 1] + p[count]))
        pArr.append(pHatn)
        if (abs(pHatn[count]-pHatn[count - 1]) < tol):
            ier = 0
            xCol = np.array(xArr, order = 'F')
            return [xCol,ier]

    pHatn = np.subtract(p[count], ((p[count + 1] - p[count]) ** 2) / (p[count+ 2] - 2 * p[count + 1] + p[count]))
    xCol = np.array(xArr, order = 'F')
    ier = 1
    return [xCol, ier]

driver()
