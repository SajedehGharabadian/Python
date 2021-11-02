name = input("enter your name:")
family=input("enter your family:")

score1=float(input("enter your lesson score1:"))
score2=float(input("enter your lesson score2:"))
score3=float(input("enter your lesson score2:"))

average = round((score1+score2+score3)/3,2)

if average >= 17 :
    print("Great!" ,"\n " , "average:" , average)
elif average>= 12 and average <17 :
    print("Normal!" , "\n" , "average:" , average)
else:
    print("Fail!" , "\n" , "average:" , average)