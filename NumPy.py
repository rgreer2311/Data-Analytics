#Numpy
import numpy as np

##Rank 1 array
arr1=[3,4,5,6,7]
print(type(arr1))

narr1=np.array(arr1)

# multidimensional array
arr2=[[1,2,3,4],[3,4,5,6]]
narr2=np.array(arr2)
print(narr2)

arr3=[[1,2,3,4],[3,4,5,6],[7,8,9,6]]
narr3=np.array(arr3)
print(narr3)

print(narr3.shape)

#2*2 array with 0s
zer=np.zeros((2,2))
print(zer)

#2*2 array with 5
full=np.full((2,2),5)
print(full)

ex3 = np.eye(4,4) #diagonal 1
print(ex3)

#concatenate two numpy arrays
x=np.array([2,6,8,4])
y=np.array([11,8,2])
z=np.concatenate([x,y])
print(z)

arr=[[1,2,3,4],[3,4,5,6],[7,8,9,6],[12,7,10,9],[2,11,8,10]]
narr=np.array(arr) #convert array into numpy array
print (narr)
