import random 


while True:
    start = input("enter  Y/N :").upper()
    if start == 'Y':
        x = random.randint (1,6)
        if x== 6 :
            print("you win!")
            continue
        else :
            break
    else:
        break