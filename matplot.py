import numpy as np
'''
arry = np.array([34, 89, 34, 90])
print(arry)
print(type(arry))
print(np.__version__)
arry = np.array(45)
print(arry)

#2D - an array that contain 1D array as its contents

arry = np.array([[34,54,9, 90], [3, 8, 9, 0], [3, 89, 0]])
#3D
arry = np.array([[[3, 9, 9], [34, 89, 90]], [[54, 89, 90], [34, 89, 90, 34]]])
arry = np.array([[[[[1, 3, 5]]]]])
print(arry)
print(arry.ndim)

arry = np.array([2, 5, 8], ndmin=6)
print(arry)
print(arry.ndim)

arry = np.array([3, 4, 8, 9, 1])
print(arry[0])
print(arry[-1])

arry1 = np.array([34, 5, 9, 3, 2, 0])
print(arry[1] + arry[3])

arry = np.array([[3, 3, 8, 9], [3, 9, 6, 0]])

print(arry)

print(arry[0][1])
'''
arry = np.array([[[1,2, 3], [4, 8, 9], [7, 9, 0]]])
print(arry[0, 1, 2])
