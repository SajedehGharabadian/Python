
m = int(input("enter first number :"))
n = int(input("enter second number :"))

i=1
if m < n :
    temp = m 
    m = n 
    n = temp
while True :
    x = m * i
    if x % n == 0 : 
        lcm = x
        break
    i = i + 1
    
print(lcm)       
