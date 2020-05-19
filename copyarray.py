from numpy import *
arr1=array([2,6,8,1,3])
arr2=arr1
print('address of arr1 is {} and value is {}'.format(id(arr1),arr1))
print('address of arr2 is {} and value is {}'.format(id(arr2),arr2))

# shallow copy
arr3=arr1.view() # shallow copy means changing the value at 1st array will reflect in 2nd array as well. vice-versa is also correct
print('address of arr3 is {} and value is {}'.format(id(arr3),arr3))

arr1[1]=7
print('============= shallow copy ===============')
print('address of arr1 is {} and value is {}'.format(id(arr1),arr1))
print('address of arr3 is {} and value is {}'.format(id(arr3),arr3))

# deep copy means changing the value at 1st array will not reflect in 2nd array.vice-versa is also correct
arr4=arr1.copy()
print('address of arr1 is {} and value is {}'.format(id(arr1),arr1))
print('address of arr4 is {} and value is {}'.format(id(arr4),arr4))

arr1[0]=1000
print('============= deep copy ===============')
print('address of arr1 is {} and value is {}'.format(id(arr1),arr1))
print('address of arr4 is {} and value is {}'.format(id(arr4),arr4))


