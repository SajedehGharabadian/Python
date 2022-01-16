
n = int(input("enter number :"))
fibo = []
i=1

while(i <= n) :
    if i == 1 :
        fibo.append(1)
    elif i == 2 :
        fibo.append(1)
    else:
        fibo.append(fibo[-2] + fibo[-1])
    
    i=i+1

print(fibo)