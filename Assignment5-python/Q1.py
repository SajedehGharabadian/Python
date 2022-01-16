import numpy as np



def Khayyam_Pascal_Triangle(n):
    x = np.ones((n+1,n+1))

    print(x)

    for i in range (1,n):
        for j in range(i):
            x[i+1][j+1] = x[i][j] + x[i][j+1]

    print(x)
   
    for i in range(n+1):
        for j in range(i+1):
            print(int(x[i][j]) , end='\t')
        print()


Khayyam_Pascal_Triangle(5)

Khayyam_Pascal_Triangle(6)

Khayyam_Pascal_Triangle(7)