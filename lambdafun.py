from functools import reduce
'''f=lambda a:a*a
result=f(5)'''
f=lambda a,b:a+b
result=f(5,6)
print(result)

nums=[3,2,6,7,8,9,5,4,0]
even=list(filter(lambda n:n%2==0,nums))
odd=list(filter(lambda n:n%2!=0,nums))
print(even)
print(odd)
double=list(map(lambda n:n*2,even))
print(double)
sum=reduce(lambda a,b:a+b,double)
print(sum)


