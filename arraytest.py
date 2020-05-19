'''import array as arr
vals=arr.array() '''

from array import *
vals = array('i',[5,8,6,3,9,4,1,2])
#print(vals.buffer_info())
'''for i in range(len(vals)):
    print(vals[i])

for e in vals:
    print(e)

chars=array('u',['a','e','i','o','u'])
print(chars)

for e in chars:
    print(e)

newArr=array(vals.typecode,(a*a for a in vals))
print('Content of newArr are:')
for e in newArr:
    print(e)
'''
arr1=array('i',[])
n=int(input("Enter The Size of Array:"))
for i in range(n):
    x=int(input("Enter The Next Value:"))
    arr1.append(x)
for e in arr1:
    print(e)

##### searching an element in an array
number_to_be_serach=int(input("Enter The number to be searched:"))
k=0
for e in arr1:
    if e==number_to_be_serach:
        print('Element {} is found in array at index {}'.format(number_to_be_serach,k))
        break
    k+=1
else:
    print('Element {} is not found in array'.format(number_to_be_serach))

print(arr1.index(number_to_be_serach))
