
def space () :
    senteces = input("enter your sentences :")
    count = 1
    print(len(senteces))
    if len(senteces) == 0 :
        print("enter sentences again")
        exit()
    for i in range (len(senteces)) :
        if senteces [i] == " " :
            count = count + 1 

    print(count)

space()