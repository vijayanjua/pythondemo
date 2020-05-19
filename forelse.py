nums=[12,13,23,21,19,16]
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print('not found')