
def Multiplication_table(m , n) :


    for i in range (1, m+1) :
        for j in range(1 , n+1) :
            print(repr(i*j).rjust(4) , end =' ')

        print("\n")
        
        
Multiplication_table(10 , 10)

Multiplication_table(5,6)

