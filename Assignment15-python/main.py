import random
import qrcode
import telebot
from gtts import gTTS
from khayyam import JalaliDate

mybot = telebot.TeleBot("token")

mymarkup = telebot.types.ReplyKeyboardMarkup()
game_btn = telebot.types.KeyboardButton('🎮New Game')

mymarkup.add(game_btn)

the_number = None
second_num = None

@mybot.message_handler(commands=['start'])
def send_welcome(message):
    msg = mybot.send_message(message.chat.id,"Hi "+str(message.chat.first_name)+" welcome to mybot"+" "+"please enter /help and bot help you")


@mybot.message_handler(commands=['game'])
def send_game(message):
    msg = mybot.reply_to(message,"Enter guess number(1,100):")
    global the_number
    the_number = random.randint(1,50)
    mybot.register_next_step_handler(msg,check_number)
    
    @mybot.message_handler(func= lambda message:True)
    def new_game(message):
        if message.text == '🎮New Game':
            msg = mybot.reply_to(message,"Enter guess number(1,100):")
            global the_number
            the_number = random.randint(1,50)
            mybot.register_next_step_handler(msg,check_number)
        
def check_number(message):
    global the_number
    try:
        if int(message.text) > the_number:
            mesg = mybot.reply_to(message,'your number is greater than random number!')
            mybot.register_next_step_handler(mesg,check_number)

        elif int(message.text) < the_number:
            mesg = mybot.reply_to(message,'your number is smaller than guess number!')
            mybot.register_next_step_handler(mesg,check_number)


        elif int(message.text) == the_number:
            mybot.reply_to(message,'you win',reply_markup= mymarkup)

    except ValueError:
        mybot.send_message(message.chat.id, "you must enter an integer")
    


age_list = []
@mybot.message_handler(commands=['age'])
def send_age(message):
    msg = mybot.reply_to(message,"Enter your age w/m/d:")

    mybot.register_next_step_handler(msg,birth_to_age)

def birth_to_age(message):
    rows = message.text.split('/')
    # for i in range(len(rows)):
    #     age_list.append(int(rows[i]))
    years = rows[0]
    months = rows[1]
    days = rows[2]

    age = JalaliDate.today() - JalaliDate(years,months,days)
    day = age.days

    year = day // 365
    remain = day % 365
    month = remain // 30
    day_s = remain % 30
    mybot.send_message(message.chat.id,"years: "+str(year)+ " "+"month:"+str(month)+" "+"days:"+str(day_s))



@mybot.message_handler(commands=['voice'])
def send_voice(message):
    msg = mybot.reply_to(message,"Enter your sentences:")

    mybot.register_next_step_handler(msg,text_to_voice)

def text_to_voice(message):
    language = 'en'
    myobj = gTTS(message.text ,lang= language , slow= False)
    myobj.save("voice1.mp3")
    my_audio = open("voice1.mp3",'rb')
    mesg = mybot.send_audio(message.chat.id, my_audio)




@mybot.message_handler(commands=['max'])
def send_max(message):
    
    msg = mybot.reply_to(message,"Enter your number list(split with(-)):")

    mybot.register_next_step_handler(msg,search_max)

def search_max(message):
    max_num = 0
    num_list = []
    try:
        rows = message.text.split('-')
        for i in range(len(rows)):
            num_list.append(int(rows[i]))
        
        max_num = max(num_list)
        
        mesg = mybot.send_message(message.chat.id,"biggest number =  "+ " "+ str(max_num))
    except ValueError:
        mybot.send_message(message.chat.id, "Wrong!")


@mybot.message_handler(commands=['argmax'])
def send_argmax(message):
    msg = mybot.reply_to(message,"Enter your number list(split with(-)):")

    mybot.register_next_step_handler(msg,search_argmax)

def search_argmax(message):
    index_num_list = []
    try:
        rows = message.text.split('-')
        for row in rows:
            index_num_list.append(int(row))
        
        for num in index_num_list:
            print(num)
        
        max_num = max(index_num_list)
        #print(max_num)
        max_index = index_num_list.index(max_num)
        print(max_index)
        
        mybot.send_message(message.chat.id, 'biggest number index: '+str(max_index))
        #max_index = 0
        
        
    except ValueError:
        mybot.send_message(message.chat.id, "Wrong!")



@mybot.message_handler(commands=['qrcode'])
def send_qrcode(message):
    msg = mybot.reply_to(message,"Enter your sentences:")

    mybot.register_next_step_handler(msg,text_to_qrcode)

    #@mybot.message_handler(func= lambda message:True)
def text_to_qrcode(message):
    img = qrcode.make(message.text)
    img.save('qrcode.png')
    photo = open('qrcode.png','rb')
    mybot.send_photo(message.chat.id,photo)

    


@mybot.message_handler(commands=['help'])
def send_help(message):
    my_file = open('help.txt','r')
    file = my_file.read()
    mybot.send_message(message.chat.id,file)

mybot.enable_save_next_step_handlers(delay=2)
mybot.load_next_step_handlers()

mybot.polling()