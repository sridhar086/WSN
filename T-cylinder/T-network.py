#! ~/anaconda/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:28:49 2015

@author: rsridhar
"""


import pandas as pa
import numpy as np
import scipy.spatial as sp
import scipy.misc as spm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def cylinder():
    centre1 = np.array((10,10,10))
    a = np.reshape(centre1,(1,3))
    rad = 2;
    angle = np.zeros(36)
    for i in range(0,36):
            angle[i] = 10*i

    #print angle
    angle = np.deg2rad(angle)
    #angle = np.array((0,30,60,90,120,150,180,210,240,270,300,330))
    
    #different angle vector that cuts open a piece in the centre of cylinder
    va = 23
    new_angle = np.zeros(27)
    
    for i in range(0,27):
        if i<= 13:
            new_angle[i] = 10*i
        if i >= 14:
            new_angle[i] = 10*va
            va = va +1
    
    
    #print new_angle     
    new_angle = np.deg2rad(new_angle)
    new_x = np.empty(27)
    new_x.fill(10)
    new_x=np.reshape(new_x,(27,1))
    
    new_cos = np.multiply(rad,np.cos(new_angle))
    new_sin = np.multiply(rad,np.sin(new_angle))
    new_y = np.reshape(np.add(10,new_cos),(27,1))
    new_z = np.reshape(np.add(10,new_sin),(27,1))
    #The code to create varying angle to cut open a piece of cylinder is done
    #the usage is done inside the loop that extends a cylinder
    
    #The piece of code that is used to add extra points while cutting the cylinder1 open
    va = 21
    new_angle1 = np.zeros(31)
    
    for i in range(0,31):
        if i<= 15:
            new_angle1[i] = 10*i
        if i >= 16:
            new_angle1[i] = 10*va
            va = va +1
    
    new_angle1 = np.deg2rad(new_angle1)
    new_x1 = np.empty(31)
    new_x1.fill(10)
    new_x1=np.reshape(new_x1,(31,1))
    
    new_cos1 = np.multiply(rad,np.cos(new_angle1))
    new_sin1 = np.multiply(rad,np.sin(new_angle1))
    
    new_y1 = np.reshape(np.add(10,new_cos1),(31,1))
    new_z1 = np.reshape(np.add(10,new_sin1),(31,1))
    
    #the code ends here
    
    
    
    
    
    
    fig = plt.figure()
    ax = Axes3D(fig)
      
    # This piece is to create the first circle with 10,10,10 as the centre
    
    cos = np.multiply(rad,np.cos(angle))
    sin = np.multiply(rad,np.sin(angle))
    y1 = np.reshape(np.add(10,cos),(36,1))
    z1 = np.reshape(np.add(10,sin),(36,1))
    x1 = np.empty(36)
    x1.fill(10)
    x1 = np.reshape(x1,(36,1))
    res1 = np.concatenate((x1,y1,z1),axis=1)
    #print res1.shape
    ax.scatter(x1,y1,z1)
    
    # this piece extends the circle to a cylinder
    i = 0.5
    var = 1
    while var == 1:
        #the below conditional part is to cut open a piece in the cylinder
        if i==3 or i==7:
            change_x = np.add(i,new_x1)
            ax.scatter(change_x,new_y1,new_z1)
            temp = np.concatenate((change_x,new_y1,new_z1),axis=1)
            res1 = np.concatenate((res1,temp))
            i = i + 0.5
            continue
        if i>3 and i<7:
            change_x = np.add(i,new_x)
            ax.scatter(change_x,new_y,new_z)
            temp = np.concatenate((change_x,new_y,new_z),axis=1)
            res1 = np.concatenate((res1,temp))
            i = i + 0.5
            continue
        change_x = np.add(i,x1)
        ax.scatter(change_x,y1,z1)
        temp = np.concatenate((change_x,y1,z1),axis=1)
        res1 = np.concatenate((res1,temp))
        if(i == 10):
            break
        i = i + 0.5
    print res1.shape
    
    
    
    
    
    
    #The below code is to add small piece add the end to finish the T joint 
    #adding one extra circle to the cylinder 2 with varying degrees
    
    va = 4
    vb = 22
    new_angle = np.zeros(22)
    
    for i in range(0,22):
        if i<= 10:
            new_angle[i] = 10*va
            va = va+1
        if i >= 11:
            new_angle[i] = 10*vb
            vb = vb +1
    
    
    print new_angle     
    new_angle = np.deg2rad(new_angle)
    new_x = np.empty(22)
    new_x.fill(8.5)
    new_x=np.reshape(new_x,(22,1))
    
    new_cos = np.multiply(rad,np.cos(new_angle))
    new_sin = np.multiply(rad,np.sin(new_angle))
    new_y = np.reshape(np.add(15,new_cos),(22,1))
    new_z = np.reshape(np.add(10,new_sin),(22,1))
    
    ax.scatter(new_y,new_x,new_z)
    temp = np.concatenate((new_y,new_x,new_z),axis=1)
    res1 = np.concatenate((res1,temp))
    
    #the one circles code ends here
    
    x2 = np.reshape(np.add(15,cos),(36,1))
    z2 = np.reshape(np.add(10,sin),(36,1))
    y2 = np.empty(36)
    y2.fill(8)
    y2 = np.reshape(y2,(36,1))
    
    
    ax.scatter(x2,y2,z2)
    temp = np.concatenate((x2,y2,z2),axis=1)
    res1 = np.concatenate((res1,temp))
    
    change_y = y2
    print change_y.shape
    i = 7.5
    var = 1
    while var == 1:
        change_y.fill(i)
        ax.scatter(x2,change_y,z2)
        temp = np.concatenate((x2,change_y,z2),axis=1)
        res1 = np.concatenate((res1,temp))
        if(i == 1):
            break
        i = i - 0.5
    
    print res1.shape
    np.save('T.npy',res1)
    
    plt.show()         
    circle = np.zeros((12,3))
    #for num in angle:

        
    
    
if __name__=='__main__':
    cylinder()
    
