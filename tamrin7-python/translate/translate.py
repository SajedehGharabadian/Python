
def show_menue():
    print("1- Add new word")
    print("2- translation english2persian")
    print("3- translation persian2english")
    print("4- show dictionary file")
    print("5- save and exit")

mywords = []

def initialize():
    try:
        f = open('translate.txt' , 'r')
        rows = f.read().split('\n')

        for i in range(0,len(rows) , 2):
            En_word = rows[i]
            Pr_word = rows[i+1]
            mywords.append({'english' : En_word , 'persian' : Pr_word })
        f.close()
    except:
        print('file not found!')

def add_word():
    flag = True
    English_word = input('enter english word:')
    for i in range(len(mywords)):
        if mywords[i]['english'] == English_word:
            flag = False
            print('please enter new word')
            break
    if flag == True:        
        Persian_word = input('enter persian word:')
        mywords.append({'english' : English_word , 'persian' : Persian_word })
        print(len(mywords))

def menue_sentences():
    print('1- Enter a sentences:')
    print('2- Enter a few sentences:')
    print('3- end translation')

def translation_English_Persian():
    while True:
        menue_sentences()
        choice = int(input('please choose from menue'))
        if choice == 1 :
            sentence = input('please enter your sentence:')
            word_sen = sentence.split(' ')
            for i in range(len(word_sen)):
                for j in range(len(mywords)):
                    if word_sen[i] == mywords[j]['english']:
                        print(mywords[j]['persian'] , end=' ')
                        break
            print()
        elif choice == 2:
            sentences = input('please enter your sentences:')
            sentence = sentences.split('.')
            for i in range(len(sentence)):
                word_sen = sentence[i].split(' ')
                for i in range(len(word_sen)):
                    for j in range(len(mywords)):
                        if word_sen[i] == mywords[j]['english']:
                            print(mywords[j]['persian'] , end=' ')
                            break
                print()
        elif choice == 3:
            break
        else:
            print('value error')

def translation_Persian_English():
     while True:
        menue_sentences()
        choice = int(input('please choose from menue'))
        if choice == 1 :
            sentence = input('please enter your sentence:')
            word_sen = sentence.split(' ')
            for i in range(len(word_sen)):
                for j in range(len(mywords)):
                    if word_sen[i] == mywords[j]['persian']:
                        print(mywords[j]['english'] , end=' ')
                        break
            print()
        elif choice == 2:
            sentences = input('please enter your sentences:')
            sentence = sentences.split('.')
            for i in range(len(sentence)):
                word_sen = sentence[i].split(' ')
                for i in range(len(word_sen)):
                    for j in range(len(mywords)):
                        if word_sen[i] == mywords[j]['persian']:
                            print(mywords[j]['english'] , end=' ')
                            break
                print()
        elif choice == 3:
            break
        else:
            print('value error')

def show_list():
     for i in range(len(mywords)):
        print(mywords[i]['english'] , '\t' , mywords[i]['persian'])

def save_and_exit():
    f = open('translate.txt' , 'w')
    for i in range(2*len(mywords)):
        if i == 0:
            row = mywords[i]['english'] + '\n' + mywords[i]['persian']
            f.write(row)
        if i < (len(mywords)-1):
            row ='\n' +mywords[i]['english'] + '\n' + mywords[i]['persian']
            f.write(row)
        if i == (len(mywords)-1) :
            row = '\n' + mywords[i]['english'] + '\n' + mywords[i]['persian']
            f.write(row)

    f.close()
    exit()

initialize()

while True:
    show_menue()
    choice = int(input("pleas choose a number :"))
    if choice == 1 :
        add_word()
    elif choice == 2:
        translation_English_Persian()
    elif choice == 3:
        translation_Persian_English()
    elif choice == 4:
        show_list()
    elif choice == 5:
        save_and_exit()