# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib import cm as CM

def add (x, y):
    return [x[0]+y[0],x[1]+y[1]]
    
def mult(x,y):
    return [x[0]*y[0]-x[1]*y[1],x[0]*y[1]+y[0]*x[1]]
    
def mandel(x,y):
    return add(mult(x,x),y)
    
def mag(x):
    return x[0]*x[0]+x[1]*x[1]

# Graph parameters    
N_X = 500
N_Y = 500
#center_X = 0.25896805
#center_Y = -0.00133482
#length_X = 0.00000001
center_X = 0
center_Y = 0
length_X = 4 
length_Y = length_X

offset_X = center_X - length_X/2
offset_Y = center_Y + length_Y/2
step_X =  length_X /  N_X
step_Y =  length_Y /  N_Y
MAX_ITERATIONS = 40    
ans = [[0 for i in range(N_X)]for j in range(N_Y)]
space = [[[i*step_X+offset_X,-j*step_Y+offset_Y] for i in range(N_X)] for j in range(N_Y)]


for i in range(N_X):
    for j in range(N_Y):
        a = space[i][j]
        temp = a
        for k in range(MAX_ITERATIONS):
            temp = mandel(temp,a)
            if(mag(temp) > 4):
                ans[i][j] = k
                break

fig = plt.figure()
mandel = fig.add_subplot(111)
mandel.imshow(ans,extent = [offset_X ,offset_X + length_X,offset_Y - length_Y,offset_Y], cmap = CM.jet)#,norm = matplotlib.colors.LogNorm())
mandel.set()
#plot.xlims([center_X - length_X/2, center_X + length_X/2])
#mandel.axis([center_X - length_X/2, center_X + length_X/2,center_Y - length_Y/2, center_Y + length_Y/2])
