weight=float(input("enter your weight(kg):"))
Height=float(input("enter your height(m):"))

BMI=weight/(Height**2)

if BMI < 18.5 :
    print("UNDERWEIGHT!")
elif BMI >= 18.5 and BMI <= 24.9 :
    print("NORMAL!")
elif BMI >= 25 and BMI <= 29.9:
    print("OVERWEIGHT!")
elif BMI >= 30 and BMI <= 34.9 :
    print("OBESE!")
else :
    print("EXTREMELY OBESE!")