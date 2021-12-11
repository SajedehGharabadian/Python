import random

options = ['Rock' , 'Paper' , 'Scissor']
scores = {'user': 0 , 'computer': 0}

for i in range(10):
    computer_choice = random.choice(options)

    user_choice = input('play the game:')

    if user_choice == computer_choice :
        print('No player gets points')

    elif computer_choice == 'Scissor':
        if user_choice == 'Rock':
            scores['user'] += 1
        elif user_choice == 'Paper':
            scores['computer'] += 1
    
    elif computer_choice == 'Rock':
        if user_choice == 'Paper':
            scores['user'] += 1
        elif user_choice == 'Scissor':
            scores['computer'] += 1
    
    elif computer_choice == 'Paper':
        if user_choice == 'Rock':
            scores['computer'] += 1
        elif user_choice == 'Scissor':
            scores['user'] += 1

    if scores['user'] == 3 :
        print('you win')
        exit()
    elif scores['computer'] == 3:
        print('computer win')
        exit()