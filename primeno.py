'''
num=int(input("Enter the number to be checked for prime:"))
for i in range(2,num):
    if num%i==0:
        print('Not Prime')
        break
else:
    print('Prime')
'''
n1=int(input('Enter the first number:'))
n2=int(input('Enter the second number:'))
for i in range(n1,n2+1):
    if i>1:
        for j in range(2,int(i/2+1)):
            if i%j==0:
                break
        else:print(i)