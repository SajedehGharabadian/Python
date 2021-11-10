import random

n=int(input("enter array size :"))
array=[]

while len(array) < n :
    x= random.randint(1,20)

    if x not in  array:
        array.append(x)
    

print(array)
