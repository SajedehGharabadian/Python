
m = int(input("enter first number :"))
n = int(input("enter second number :"))

if n > m :
    small_num = m 
else :
    small_num = n


for i in range (1,small_num+1) :
    if ((n %i == 0) and (m % i == 0)) :
        gcd = i

print(gcd)

