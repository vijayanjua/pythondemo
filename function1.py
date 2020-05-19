#positional actual argument
def person(name,age=6):
    print(name)
    print(age-5)

person('vijay',30)

# keyword actual arguments
person(age=30,name='Romika')

# default actual arguments
person('Reyansh')

# variable length arguments
def sum(a,*b):
    #print(a)
    #print(b)
    c=a
    for x in b:
        c+=x
    print(c)

sum(34,56,71,68,97)


# keyword variable arguments           # instead of kwargs we can use different name as well.
def person1(name,**kwargs):
    print(name)
    for i,j in kwargs.items():
        print(i,j)

person1('Vijay',age=30,city='gurugram',mob='9874563210')

a=10
b=20
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(x))
    print('in fun ',a)
    globals()['a']=100
    print('in func',a)

something()
print('in outside',a)

