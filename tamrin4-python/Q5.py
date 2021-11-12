
def factorial(x) :
    n=1
    y=1

    while (n <=  x//2) :
        y = y * n 
        if ( y > x) :
            print("No")
            break
        elif y == x :
            print("yes")
            break
        n = n + 1

factorial(24)

factorial(6)

factorial(120)

factorial(26)
