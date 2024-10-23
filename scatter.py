import matplotlib as mtp
import numpy as np

x1=np.array([0,1,5,7,8,10,12])
y1=np.array([2,6,8,5,2,12,18])
mtp.scatter(x1,y1)

x2=np.array([1,4,6,8,10,12,15])
y2=np.array([0,5,10,4,8,6,12])
mtp.scatter(x2, y2, marker="*")