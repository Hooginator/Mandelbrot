# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib import cm as CM
import numpy as np
import os

def add (x, y):
    return [x[0]+y[0],x[1]+y[1]]
    
def mult(x,y):
    return [x[0]*y[0]-x[1]*y[1],x[0]*y[1]+y[0]*x[1]]
    
def mandel(x,y):
    return add(mult(x,x),y)
    
def mag(x):
    return x[0]*x[0]+x[1]*x[1]

def getSpace(N_X, N_Y, X, Y, dX,dY):
    # Takes the central position, number of X, Y coordinates to use
    # and the distance between each point
    
    ans = [[0 for i in range(N_X)]for j in range(N_Y)]
    space = [[[(i-N_X/2)*dX+X,-(j-N_Y/2)*dY+Y] for i in range(N_X)] for j in range(N_Y)]
    return [ans,space]

def domandel(nX,nY,cX,cY,dX, dY, MAX_ITERATIONS):
    [ans, space] = getSpace(nX,nY,cX,cY,dX, dY)    
    for i in range(nX):
        for j in range(nY):
            a = space[i][j]
            temp = a
            for k in range(MAX_ITERATIONS):
                temp = mandel(temp,a)
                if(mag(temp) > 4):
                    ans[i][j] = k
                    if(k==0):
                        ans[i][j] = 0.1
                    break
                if(k == MAX_ITERATIONS-1):
                    ans[i][j] = 0.1
                    break
    return ans

def doplot(toplot,cX,cY,lX,lY,n):
    # plots a colour map    
    fig = plt.imshow(toplot,extent = [cX-lX/2 ,cX+lX/2,cY-lY/2,cY+lY/2], cmap = CM.jet, norm = matplotlib.colors.LogNorm())
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig('foo'+str(n)+'.png', bbox_inches='tight', pad_inches = 0,)
    return fig

def savenumbers(ans,i,nX,nY,foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    tempfile = open(foldername + '/MandelNumbers' + str(i)+'.txt','w')
    for i in range(nX):
        for j in range(nY):
            tempfile.write("%s " % ans[i][j])
        tempfile.write("\n")
    tempfile.close()

def loadnumbers(fileName,i,nX,nY):
    return np.loadtxt(fileName + str(i) + '.txt')
    
def loadandplot(fileName,n,nX,nY):
    for i in range(n):
        doplot(loadnumbers(fileName,i,nX,nY),0,0,1,1,i)
    
def domultiplemandel(nX,nY,cX,cY,lX,lY,MAX_ITERATIONS,frames):
    for i in range(500,frames):
        [lX,lY] = [0.75*lX,0.75*lY] # Total length of the X, Y axis
        [dX,dY] = [lX/nX,lY/nY] # distance between neighbouring points
        ans = domandel(nX,nY,cX,cY,dX, dY, MAX_ITERATIONS)
        #doplot(ans,cX,cY,lX,lY,i)
        foldername = "/data/Mandel002"
        savenumbers(ans,i,nX,nY,foldername)
        #MAX_ITERATIONS +=  10
        print("Finished Mandel " +str(i)+" for l = " + str(lX))

def main():
    # Start Conditions
    MAX_ITERATIONS = 1000
    [nX, nY] = [500,500] # number of data points to take along real and imag axis
    [cX,cY] = [0.001643721971153,-0.822467633298876] # Middle of where we are looking
    [lX,lY] = [4,4] # Total length of the X, Y axis
    domultiplemandel(nX,nY,cX,cY,lX,lY,MAX_ITERATIONS, 1000)
    #abc = loadnumbers('MandelNumbers',0,nX,nY)
    #doplot(abc,cX,cY,lX,lY,0)
    #print(abc)

main()
#loadandplot('MandelNumbers',100,500,500)
os.system("shutdown now")