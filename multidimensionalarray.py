from numpy import *
'''
#arr=array([1,3,2,5,4])
#print(arr)
arr=linspace(0,15,12)
arr1=arange(0,15,2)
arr2=logspace(1,40,5)
arr3=zeros(5,int)
arr4=ones(5,int)
print('Linspace():',arr)
print('arange():',arr1)
print('logspace():',arr2)
print('zeros():',arr3)
print('ones():',arr4)

'''
arr1=array([
            [1,2,3,4,5,6],
            [4,5,6,7,8,9]

          ])
print(arr1)
print('array data type:',arr1.dtype)
print('array dimension:',arr1.ndim)
print('array shape means rows and columns:',arr1.shape)
print('array size means no of total element:',arr1.size)

print('======== conversion of two dimension array to single dimension =========')
arr2=arr1.flatten()
print('2-D array {} is converted in to 1-D array {}'.format(arr1,arr2))

print('======== conversion of single dimension array to two dimension =========')
arr3=arr2.reshape(3,4)
print('1-D array {} is converted in to 2-D array {}'.format(arr2,arr3))

print('======== conversion of single dimension array to three dimension =========')
arr4=arr2.reshape(3,2,2)
print('1-D array {} is converted in to 3-D array {}'.format(arr2,arr4))

m1=matrix('1 2 3; 6 4 5; 1 6 7')
m2=matrix('1 2 3; 6 8 5; 2 6 7')
print('diagonal of matrix m1: ', m1.diagonal())
#print('sum of matrix m1 and m2: ', m1+m2)
#print('multiplication of matrix m1 and m2: ', m1*m2)