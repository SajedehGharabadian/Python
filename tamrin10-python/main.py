from actor_class import Actor
from clip import Clip
from media_class import Media
from film import Film
from series import Series 
from documentary import Documentary


def show_menue():
    print("1- Add Media")
    print("2- Edit Media")
    print("3- Dlete Media")
    print("4- Search")
    print("5- Download")
    print("6- Show")
    print("7- Save and Exit")

Video = []
def load():
    f = open('data.txt','r')

    rows = f.read().split('\n')
    for i in range(len(rows)):
        info = rows[i].split(',')
        if info[0] == "film":
            actors = info[6].split('-')
            casts= []
            for j in range(len(actors)):
                actor = []
                actor = actors[j].split(' ') 
                cast =Actor(actor[0],actor[1])
                casts.append(cast)
            film = Film(info[0],info[1],info[2],info[3],info[4],info[5],casts)
            Video.append(film)
        elif info[0] == "serial":
            actors = info[7].split('-')
            casts = []
            for j in range(len(actors)):
                cast = actors[j].split(' ') 
                actor = Actor(cast[0],cast[1])
                casts.append(actors)
            series = Series(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8])
            Video.append(series)
        elif info[0] == "documentary":
            actors = info[7].split('-')
            casts = []
            for j in range(len(actors)):
                cast = actors[j].split(' ') 
                actor = Actor(cast[0],cast[1])
                casts.append(actors)
            documentary = Documentary(info[0],info[1],info[2],info[3],info[4],info[5],info[6],casts,info[8])
            Video.append(documentary)
        elif info[0] == "clip":
            actors = info[6].split('-')
            casts = []
            for j in range(len(actors)):
                cast = actors[j].split(' ') 
                actor = Actor(cast[0],cast[1])
                casts.append(actors)
            clip = Clip(info[0],info[1],info[2],info[3],info[4],info[5],casts)
            Video.append(clip)
    f.close()

def actor_menue():
    print('1- add actor')
    print('2- end add')

def add_media():
    type = input("enter type:")
    if type.lower() == "film":
        name = input("enter name:")
        name_dir = input("enter director name:")
        score =float(input("enter score:"))
        link = input("enter link:")
        duration = int(input("enter duration:"))
        while True:
            actor_menue()
            choice = int(input('choose from actor menue:'))
            actors = []
            if choice == 1:
                name_actor = input('enter actor name:')
                actors.append(name_actor)
            elif choice == 2:
                break
        Video.append(Film(type,name,name_dir,score,link,duration,actors))
        print('New products added successfully')

    elif type.lower() == "serial":
        name = input("enter name:")
        name_dir = input("enter director name:")
        score =float(input("enter score:"))
        link = input("enter link:")
        duration = int(input("enter duration:"))
        while True:
            actor_menue()
            choice = int(input('choose from actor menue:'))
            actors = []
            if choice == 1:
                name_actor = input('enter actor name:')
                actors.append(name_actor)
            elif choice == 2:
                break
        part = int(input('enter part:'))
        season = int(input('enter season:'))
        Video.append(Series(type,name,name_dir,score,link,duration,part,actors,season))
        print('New products added successfully')
    elif  type.lower() == "documentary":
        name = input("enter name:")
        name_dir = input("enter director name:")
        score =float(input("enter score:"))
        link = input("enter link:")
        duration = int(input("enter duration:"))
        while True:
            actor_menue()
            choice = int(input('choose from actor menue:'))
            actors = []
            if choice == 1:
                name_actor = input('enter actor name:')
                actors.append(name_actor)
            elif choice == 2:
                break
        part = int(input('enter part:'))
        season = int(input('enter season:'))
        Video.append(Documentary(type,name,name_dir,score,link,duration,part,actors,season))
        print('New products added successfully')
    elif type.lower() == "clip":
        name = input("enter name:")
        name_dir = input("enter director name:")
        score =float(input("enter score:"))
        link = input("enter link:")
        duration = int(input("enter duration:"))
        while True:
            actor_menue()
            choice = int(input('choose from actor menue:'))
            actors = []
            if choice == 1:
                name_actor = input('enter actor name:')
                actors.append(name_actor)
            elif choice == 2:
                break
        Video.append(Clip(type,name,name_dir,score,link,duration,actors))
        print('New products added successfully')

def show_edit_menue():
    print('1- type')
    print('2- director name')
    print('3- score')
    print('4- link')
    print('5- duration')
    print('6- end edit ')

def edit_media():
    name = input("enter name:")
    for i in range(len(Video)):
       # media = Media()
        if Video[i].name == name:
            while True:
                show_edit_menue()
                choice = int(input('please choose from edit menue:'))

                if choice == 1:
                    Video[i].type = input('please enter new type:')
                elif choice == 2:
                    Video[i].director = input("please enter new name of director:")
                elif choice == 3:
                    Video[i].score = float(input("please enter new score:"))
                elif choice == 4:
                    Video[i].link = input('please enter new link:')
                elif choice == 5:
                    Video[i].duration = int(input('please enter new duration:'))
                elif choice == 6:
                    break
                else:
                    print('value error')

def delete_media():
    name = input("enter name:")
    for i in range(len(Video)):
        if Video[i].name == name:
            Video.pop(i)
            print('Product removed!')
            break       

def search_media():
    result = []
    time1 = int(input('please enter min time:'))
    time2 = int(input('please enter max time:'))
    for i in range(len(Video)):
        if time1 < int(Video[i].duration) < time2 and Video[i].type == 'film':
            result.append(Video[i].name)

    for j in range(len(result)):
        print(result[j])

def download():
    name = input('please enter name:')
    for i in range(len(Video)):
        if Video[i].name == name:
            Video[i].download()
            print('download')

def save_and_exit():
    f = open('data.txt','w')
    for i in range(len(Video)):
        if i < (len(Video)-1):
            row = Video[i].type +','+ Video[i].name +','+ Video[i].director +','+ str(Video[i].score).format() +','+Video[i].url +','+ str(Video[i].duration).format() + '\n'
            f.write(row)
        if i == (len(Video)-1):
            row = Video[i].type +','+ Video[i].name +','+ Video[i].director +','+ str(Video[i].score).format() +','+Video[i].url +','+ str(Video[i].duration).format()  
            f.write(row)  
        
    f.close()
    exit()     

def show():
    for m in Video:
        m.show_info()

load()

while True:
    show_menue()
    choice = int(input("please choose number:"))

    if choice == 1:
        add_media()
    elif choice == 2:
        edit_media()
    elif choice == 3:
        delete_media()
    elif choice == 4:
        search_media()
    elif choice == 5:
        download()
    elif choice == 6:
        show()
    elif choice == 7:
        save_and_exit()
