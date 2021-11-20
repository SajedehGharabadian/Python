import time
import random
from termcolor import colored


print("choose 1.single player 2.two player :")

choose = input("choose option:")

counter = 0

start = time.time()
def show_game_boeard():
    for i in range (3):
        for j in range (3):
            print(game[i][j] , end=" ")

        print()

def information (taw) : 
    while True :
        row = int(input("enter row:" ))
        col = int(input("enter column:"))

        if   0 <= row <= 2 and 0 <= col <= 2 :
            if game[row][col] == '_':
                game[row][col] = taw
                break
            else:
                print("cell is not empty")
        else:
            print("index out of range , try again!")

def check_com() :
    j=0
    for i in range (3):
       if game[i][j] == game[i][j+1] == game[i][j+2] == colored("X" ,'blue'):
            print("player1 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
       elif game[i][j] == game[i][j+1] == game[i][j+2] == colored("O" ,'red') :
            print("player2 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
    i=0
    for j in range(3):
       if game[i][j] == game[i+1][j] == game[i+2][j] == colored("X" ,'blue'):
            print("player1 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
       elif game[i][j] == game[i+1][j] == game[i+2][j] == colored("O" ,'red') :
            print("player2 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
    k=0
    if game[k][k] == game[k+1][k+1] == game[k+2][k+2] == colored("X" ,'blue'):
        print("player1 win")
        exit()
    elif game[k][k] == game[k+1][k+1] == game[k+2][k+2] == colored("O" ,'red') :
        print("player2 win")
        print("Run Time: " + str( time.time() - start ))
        exit()   
    j=2
    i=0
    if game[i][j] == game[i+1][j-1] == game[i+2][j-2] == colored("X" ,'blue'):
        print("player1 win")
        print("Run Time: " + str( time.time() - start ))
        exit()
    elif game[i][j] == game[i+1][j-1] == game[i+2][j-2] == colored("O" ,'red') :
        print("player2 win")
        print("Run Time: " + str( time.time() - start ))
        exit()  



def check() :
    #flag =True
    j=0
    for i in range (3):
       if game[i][j] == game[i][j+1] == game[i][j+2] == colored("X" ,'yellow'):
            print("player1 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
       elif game[i][j] == game[i][j+1] == game[i][j+2] == colored("O" ,'red') :
            print("player2 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
    i=0
    for j in range(3):
       if game[i][j] == game[i+1][j] == game[i+2][j] == colored("X" ,'yellow'):
            print("player1 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
       elif game[i][j] == game[i+1][j] == game[i+2][j] == colored("O" ,'green') :
            print("player2 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
    k=0
    if game[k][k] == game[k+1][k+1] == game[k+2][k+2] == colored("X" ,'yellow'):
        print("player1 win")
        exit()
    elif game[k][k] == game[k+1][k+1] == game[k+2][k+2] == colored("O" ,'green') :
        print("player2 win")
        print("Run Time: " + str( time.time() - start ))
        exit()   
    j=2
    i=0
    if game[i][j] == game[i+1][j-1] == game[i+2][j-2] == colored("X" ,'yellow'):
        print("player1 win")
        print("Run Time: " + str( time.time() - start ))
        exit()
    elif game[i][j] == game[i+1][j-1] == game[i+2][j-2] == colored("O" ,'green') :
        print("player2 win")
        print("Run Time: " + str( time.time() - start ))
        exit() 
def equal(cnt):
    if cnt == 9 :
        print("the game does not win!")
        print("Run Time: " + str( time.time() - start ))
        exit()

def information_computer(taw) :
    while True :
        row = random.randint(0,2)
        col = random.randint(0,2)

        if   0 <= row <= 2 and 0 <= col <= 2 :
            if game[row][col] == '_':
                game[row][col] = taw
                break
            else:
                print("cell is not empty")
        else:
            print("index out of range , try again!")
        
game = [['_', '_' , '_'],
         ['_', '_' , '_'],
         ['_', '_' , '_'] ]

show_game_boeard()

if (str(choose) == "1") :
    while True:
        start = time.time()
        print("player1")
        information_computer(colored("X" ,'blue'))
        show_game_boeard()
        check_com()
        counter += 1
        equal(counter)

        print("player2")
        information(colored("O" ,'red'))
        show_game_boeard()
        check_com()
        counter += 1
        equal(counter)



#show_game_boeard()
if (str(choose) == "2"):
    while True :
        start = time.time()
        print("player1")
        information(colored("X" ,'yellow'))
        show_game_boeard()
        check()
        counter += 1
        equal(counter)

        print("player2")
        information(colored("O" ,'green'))
        show_game_boeard()
        check()
        counter += 1
        equal(counter)
    
    

    
    
   


