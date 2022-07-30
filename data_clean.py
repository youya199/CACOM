#import pandas as pd
import numpy as np
#import ast
#import math
import matplotlib.pyplot as plt
import csv2np
import angle
import vast_to_6_points
import visualization
from matplotlib.animation import FuncAnimation
# from matplotlib.animation import FFMpegWriter
# this file takes in one csv file, and spit one corresponding angle graph

#1. from csv to int 
X=csv2np.csv2np_fun('Extracted_point_fr250-510.csv')
#2. clean data

n_c=X.shape[1]
n_r=X.shape[0]

Y=[]
#[list([1,1]),list([2,2]),list([3,3]),list([4,4]),list([5,5]),list([6,6])]
for r in range(n_r):
    
    this_row=X[r,:]
    this_row=[x for x in this_row if x is not None]
    if len(this_row)<6:# delete the rows that consist of <6 pairs of coordinates
        continue    
    elif len(this_row)==6:#save the rows that have 6 pairs of coordinates
        # b=np.array(this_row)
        # b=b[np.newaxis,:]
        # Y=np.concatenate((Y,b),axis=0) 
        Y.append(this_row)
    else:#for rows with >6 pairs of coordinates, call delect_to_6
        data_new, num_new = vast_to_6_points.delect_to_6(this_row)
        if num_new==6:
            # revised_this_row=np.array(data_new)
            # revised_this_row=revised_this_row[np.newaxis,:]
            # Y=np.concatenate((Y,revised_this_row),axis=0) #revise the rows that have >6 pairs of coordinates
            Y.append(data_new)
        else:
            continue
            
        
    B=3


#ouput 1: draw the angle graph
list_of_angles=angle.coor2angle(Y)
visualization.visual(list_of_angles)
plt.show()

# #output 2: animation of points

# ##range calculate
# c=np.array(Y) 
# y_max=np.amax(c[:,:,0])
# y_min=np.amin(c[:,:,0])
# x_max=np.amax(c[:,:,1])
# x_min=np.amin(c[:,:,1])
# #print(y_max,y_min,x_max,x_min)

# def animate(i):
#     c=np.array(Y[i])
#     plt.cla()
#     plt.xlim([x_min, x_max])
#     plt.ylim([-y_max,-y_min])
#     plt.scatter(c[:,1],-c[:,0])
#     #i+=1

# ani = FuncAnimation(plt.gcf(), animate, interval=50)
# plt.show()

    


