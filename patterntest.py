def pattern1(n):
    k=2*n-2
    for i in range(n):
        for j in range(k):
            print(end=' ')
        k=k-1
        for j in range(0,i+1):
            print('*',end=' ')

        print()

def pattern2(n):
    k=n-1
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=' ')
        k=k+1
        for j in range(0,i):
            print('*',end=' ')

        print()

def pattern3(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()
    for i in range(n+1,0,-1):
        for j in range(0,i):
            print('*',end=' ')

        print()
def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()
    for i in range(n+1,0,-1):
        for j in range(0,i):
            print('*',end=' ')

        print()

#pattern1(10)
#pattern2(10)
pattern3(5)