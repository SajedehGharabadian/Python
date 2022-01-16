import math

op=input("enter operation:")


if op == '+' or  op == '-' or  op == '*' or op == '/' :
    a=float(input("enter first number:"))
    b=float(input("enter second number:"))
    if op == '+':
        result=a+b
        print(result)
    elif op == '-':
         result=a-b
         print(result)
    elif op == '*':
        result=a*b
        print(result)
    else :
        if b != 0:
            result=a/b
            print(result)
        else:
             print("khataa!!")


if op == 'Radical' or  op == 'sin' or  op == 'cot' or op == 'cos' or  op == 'factorial' :
    c=float(input("enter  number:")) 
    if op == 'Radical' :
        result2 = math.sqrt(c)
        print(result2)
    elif op == 'sin' :
        result2 = math.sin(math.radians(c))
        print(result2)
    elif op == 'cot' :
        result2 = math.cos(math.radians(c)) / math.cos(math.radians(c))  
        print(result2)
    elif op == 'cos' :
        result2 = math.cos(math.radians(c))
        print(result2)
    elif op == 'tan' :
        result2 = math.tan(math.radians(c))
        print(result2)
    elif op == 'factorial' :
        result2 = math.factorial(c)
        print(result2)

