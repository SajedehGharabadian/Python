import math

def second_degree_equation (a , b , c ) :
    delta = (b**2) - (4*a*c)
    print(delta)
    if delta > 0 :
        x1=((-b) + math.sqrt(delta)) / (2*a)
        x2=((-b) - math.sqrt(delta) ) / (2*a)
        print("first answer :" , x1)
        print("second answer :" , x2)

    
    elif delta == 0 :
        x = (-b) / (2*a)
        print("answer :" , x)

    else :
        print("No answer!")


second_degree_equation(5 , 2 , 1 )

second_degree_equation(1 , 0  , 4)

second_degree_equation( 1 , 0  , -4)
