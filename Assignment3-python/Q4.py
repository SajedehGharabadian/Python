
size = int(input("enter size :"))
i=1

for i in range (size) :
    if i % 2 == 0 :
        print("*" , end = ' ')
    else :
        print("#" , end = ' ')
