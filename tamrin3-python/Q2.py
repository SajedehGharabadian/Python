import random

n=int(input("enter size array :"))
array=[]

for i in range (n) :
    x= random.randint(1,20)

    if x not in  array:
        array.append(x)
    

print(array)
