#! ~/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:07:16 2015

@author: rsridhar
"""
import pandas as pa
import numpy as np
import scipy.spatial.distance as spa
from scipy.io import loadmat
from scipy.sparse.csgraph import dijkstra
import scipy as sp
import random
import matplotlib.pyplot as plt
import os
#import toHDF
import math 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


def gen_top():
    #df = pa.read_excel('orig.xlsx',header=None)
    #orig = np.array(df)
    #np.save('hourglass.npy',orig)
    orig = np.load('hourglass_coor.npy')
    print orig.shape
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(orig[:,0],orig[:,1],orig[:,2],c=orig[:,2],cmap='seismic')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    
if __name__=='__main__':
    
    gen_top()
    
