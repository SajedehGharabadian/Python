
n = int(input('enter number of rows:'))
star = '*'
space = ' '

for i in range(1,n+1):
    row = i*2 - 1
    sp = n - i
    print(sp*space , row*star)
for j in range(n-1 , 0 , -1):
    row = j*2 - 1
    sp = n - j
    print(sp*space , row*star)