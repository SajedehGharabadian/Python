import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

# i = random.randint(0, len(words)-1)
# word = words[i]

word = random.choice(words) # clock
chance = 10
right_word = []

print('- ' * len(word)) # - - - - -

while chance > 0:
    

    user_character = input().lower() 

    if user_character in word:
        
        print('yes')
        right_word.append(user_character)
        for i in range (len(word)) :
            if word[i] in right_word:
                print(word[i],end="") 
            else:
                 print("-" )
        if len(word) == len(right_word) :
            print( "you win!!" )
            break
    else:
        chance = chance - 1
        print('no')