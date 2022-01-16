
a=int(input("enter side1:"))
b=int(input("enter side2:"))
c=int(input("enter side3:"))

if a < b + c and b < a + c and c < a + b :
    print("You can draw a triangle")
else : 
    print("You can not draw a triangle")