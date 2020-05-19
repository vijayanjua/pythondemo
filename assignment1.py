for i in range(4):
    for j in range(1,5):
        if j>i:
            print(j,end=' ')
    print()

print('+++++++++++++++++++++++++++++++++++++++++++')
for k in range(4):
    for l in range(4):
        if l<=k:
            print(chr(l+65),end=' ')
        elif l>k:
            print(chr(79+l), end=' ')
    print()