a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
#b='y'
try:
    print('resource open')
    print(a/b)
    k=int(input("Enter the 3rd number:"))
    print(k)

except ZeroDivisionError as e:
    print('Hey, you can not divide a number by zero, ',e)
except ValueError as e:
    print('Invalid Input ',e)
except Exception as e:
    print('Something went wrong!, ',e)

finally:
    print('Resource Closed')