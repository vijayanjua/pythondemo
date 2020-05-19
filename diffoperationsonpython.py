from numpy import *
arr1=array([11,2,31,4,52])
arr2=array([1,2,3,4,5])

# addition of a number to each element
arr=arr1+10
print(arr)

# addition of element of two arrays ==> vectorized operation
arr3=arr1+arr2
print(arr3)

print('Sum of an array',sum(arr1))
print('Min of an array',min(arr1))
print('Max of an array',max(arr1))
print('Average of an array',average(arr1))
print('Log of an array',log(arr1))
print('Sin of an array',sin(arr1))
print('Cos of an array',cos(arr1))
print('Square root of an array',sqrt(arr1))
print('Square of an array',square(arr1))
print('concatenating array1 and array2',concatenate([arr1,arr2]))
print('Sorting of an array',sort(arr1))
