'''
av=5
av1=av
x=int(input('How Many Candies you want?: '))
for i in range(x):
    if i>av-1:
        print('Out of Stock')
        break
    print('Take candie {}'.format(i))
    #av1-=1
print('Candies left after transaction:{} and enter value: {}'.format(av1,x))


for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)
'''
for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)

