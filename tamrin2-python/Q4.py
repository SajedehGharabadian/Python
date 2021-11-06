
number_student = int(input("enter the number of student :"))
Sum = 0
grades = []

for i in range (number_student) :
    grade = float(input("grade : "))
    grades.append(grade)
    Sum += grade
    average = Sum / number_student
    
print(max(grades))
print(min(grades))
average = round(Sum / number_student , 2)
print(average )
