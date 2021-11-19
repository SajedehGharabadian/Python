import numpy as np



def Khayyam_Pascal_Triangle(n):
    x = np.ones((n,n))

    print(x)
    i=1
    for i in range (n+1):
        for j in range(1,i):
            x[i+1][j+1] = x[i][j] + x[i][j+1]

    print(x)


Khayyam_Pascal_Triangle(3)