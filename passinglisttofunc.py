
def countoddeven(lst1):
    ev=0
    od=0
    for i in lst1:
        if i%2==0:
            ev+=1
        else:
            od+=1
    return ev,od

lst=[20,25,14,19,24,16,28,47,53,37,26]
even,odd=countoddeven(lst)
print("No of Even number: {} and no of odd number: {} in list : {}".format(even,odd,lst))