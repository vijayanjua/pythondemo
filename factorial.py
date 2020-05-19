def fact(n):
    for i in range(1,n):
        n=n*i
       # if i>n-1:
        #    break
    return n
fa=fact(5)
print(fa)
