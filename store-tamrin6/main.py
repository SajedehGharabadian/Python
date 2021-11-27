from pyfiglet import Figlet
import qrcode


def show_menue():
    print("1- Add product")
    print("2- Edit product")
    print("3- Dlete Product")
    print("4- Search")
    print("5- Show List ")
    print("6- Buy")
    print("7- Exit")

PRODUCTS = []

def load():
    print("Loading...")
    myfile= open('database.txt' , 'r')
    data = myfile.read()
    product_list = data.split('\n')
    for i in range(len(product_list)):
        product_info= product_list[i].split(',')
        mydict = {}
        mydict['code'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        mydict['count'] = product_info[3]
        PRODUCTS.append(mydict)
    print('Welcom')

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def add_product():
    code = int(input("product code:"))
    name = input("product name:")
    price = int(input("product price:"))
    count = int(input("product count:"))
    myfile = open('database.txt' ,'at')
    add_dict = {}
    add_dict['code'] = code
    add_dict['name'] = name
    add_dict['price'] = price
    add_dict['count'] = count
    myfile.write('\n')
    myfile.write(str(add_dict['code']))
    myfile.write(',')
    myfile.write(add_dict['name'])
    myfile.write(',')
    myfile.write(str(add_dict['price']))
    myfile.write(',')
    myfile.write(str(add_dict['count']))

def Del_product():
    name = input("enter name product :")
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name'] == name :
            del PRODUCTS[i]['code']
            del PRODUCTS[i]['name']
            del PRODUCTS[i]['price']
            del PRODUCTS[i]['count']
            x = i
            break
    del_dict = {}
    myfile = open('database.txt' ,'wt')
    for j in range(x,(len(PRODUCTS)-1)):
        PRODUCTS[j] = PRODUCTS[j+1]
    for i in range(len(PRODUCTS)-1):
        if i < (len(PRODUCTS)-1):
            del_dict['code'] = PRODUCTS[i]['code']
            del_dict['name'] = PRODUCTS[i]['name']
            del_dict['price'] = PRODUCTS[i]['price']
            del_dict['count'] = PRODUCTS[i]['count']
            myfile.write(str(del_dict['code']))
            myfile.write(',')
            myfile.write(del_dict['name'])
            myfile.write(',')
            myfile.write(str(del_dict['price']))
            myfile.write(',')
            myfile.write(str(del_dict['count']))
        elif i == (len(PRODUCTS)-1):
            del_dict['code'] = PRODUCTS[i]['code']
            del_dict['name'] = PRODUCTS[i]['name']
            del_dict['price'] = PRODUCTS[i]['price']
            del_dict['count'] = PRODUCTS[i]['count']
            myfile.write(str(del_dict['code']))
            myfile.write(',')
            myfile.write(del_dict['name'])
            myfile.write(',')
            myfile.write(str(del_dict['price']))
            myfile.write(',')
            myfile.write(str(del_dict['count']))
        if i < (len(PRODUCTS)-2) :
            myfile.write('\n')

def edit_product():
    edit = input("What do you want to edit? ")
    myfile = open('database.txt' ,'w')
    if edit == 'code':
        product = input("print name product :")
        edit_dict = {}
        code = int(input("new code :"))
        for i in range(len(PRODUCTS)-1):
            if PRODUCTS[i]['name'] == product:
                PRODUCTS[i]['code'] = code
        for i in range(len(PRODUCTS)):
            if i < (len(PRODUCTS)-1):
                edit_dict['code'] = PRODUCTS[i]['code']
                edit_dict['name'] = PRODUCTS[i]['name']
                edit_dict['price'] = PRODUCTS[i]['price']
                edit_dict['count'] = PRODUCTS[i]['count']
                myfile.write(str(edit_dict['code']))
                myfile.write(',')
                myfile.write(edit_dict['name'])
                myfile.write(',')
                myfile.write(str(edit_dict['price']))
                myfile.write(',')
                myfile.write(str(edit_dict['count']))
            elif i == (len(PRODUCTS)-1):
                edit_dict['code'] = PRODUCTS[i]['code']
                edit_dict['name'] = PRODUCTS[i]['name']
                edit_dict['price'] = PRODUCTS[i]['price']
                edit_dict['count'] = PRODUCTS[i]['count']
                myfile.write(str(edit_dict['code']))
                myfile.write(',')
                myfile.write(edit_dict['name'])
                myfile.write(',')
                myfile.write(str(edit_dict['price']))
                myfile.write(',')
                myfile.write(str(edit_dict['count']))
            if i < (len(PRODUCTS)-1) :
                myfile.write('\n')

    if edit == 'price':
        product = input("print name product :")
        edit_dict = {}
        price = int(input("new price :"))
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['name'] == product:
                PRODUCTS[i]['price'] = price
        for i in range(len(PRODUCTS)):
            if i < (len(PRODUCTS)-1):
                edit_dict['code'] = PRODUCTS[i]['code']
                edit_dict['name'] = PRODUCTS[i]['name']
                edit_dict['price'] = PRODUCTS[i]['price']
                edit_dict['count'] = PRODUCTS[i]['count']
                myfile.write(str(edit_dict['code']))
                myfile.write(',')
                myfile.write(edit_dict['name'])
                myfile.write(',')
                myfile.write(str(edit_dict['price']))
                myfile.write(',')
                myfile.write(str(edit_dict['count']))
            elif i == (len(PRODUCTS)-1):
                edit_dict['code'] = PRODUCTS[i]['code']
                edit_dict['name'] = PRODUCTS[i]['name']
                edit_dict['price'] = PRODUCTS[i]['price']
                edit_dict['count'] = PRODUCTS[i]['count']
                myfile.write(str(edit_dict['code']))
                myfile.write(',')
                myfile.write(edit_dict['name'])
                myfile.write(',')
                myfile.write(str(edit_dict['price']))
                myfile.write(',')
                myfile.write(str(edit_dict['count']))
            if i < (len(PRODUCTS)-1) :
                myfile.write('\n')
         
    if edit == 'count':
        product = input("print name product :")
        edit_dict = {}
        count = int(input("new count :"))
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['name'] == product:
                PRODUCTS[i]['count'] = count 
        for i in range(len(PRODUCTS)):
            if i < (len(PRODUCTS)-1):
                edit_dict['code'] = PRODUCTS[i]['code']
                edit_dict['name'] = PRODUCTS[i]['name']
                edit_dict['price'] = PRODUCTS[i]['price']
                edit_dict['count'] = PRODUCTS[i]['count']
                myfile.write(str(edit_dict['code']))
                myfile.write(',')
                myfile.write(edit_dict['name'])
                myfile.write(',')
                myfile.write(str(edit_dict['price']))
                myfile.write(',')
                myfile.write(str(edit_dict['count']))
            elif i == (len(PRODUCTS)-1):
                edit_dict['code'] = PRODUCTS[i]['code']
                edit_dict['name'] = PRODUCTS[i]['name']
                edit_dict['price'] = PRODUCTS[i]['price']
                edit_dict['count'] = PRODUCTS[i]['count']
                myfile.write(str(edit_dict['code']))
                myfile.write(',')
                myfile.write(edit_dict['name'])
                myfile.write(',')
                myfile.write(str(edit_dict['price']))
                myfile.write(',')
                myfile.write(str(edit_dict['count']))
            if i < (len(PRODUCTS)-1) :
                myfile.write('\n')


Bill =[]

def buy_pro():
    while True:
        option = input("buy or finish :")
        bill = {}
        if option == 'buy':
            code_pro = int(input("enter product code :"))
            for i in range(len(PRODUCTS)):
                if int(PRODUCTS[i]['code']) == code_pro:
                    count_pro = int(input("entrer product count :"))
                    if count_pro <=  int(PRODUCTS[i]['count']):
                        new_count = int(PRODUCTS[i]['count']) - count_pro
                        PRODUCTS[i]['count'] = str(new_count)
                        bill['code'] = PRODUCTS[i]['code']
                        bill['name'] = PRODUCTS[i]['name']
                        bill['price'] = PRODUCTS[i]['price']
                        bill['count'] = str(count_pro)
                        Bill.append(bill)
                    break
        if option == 'finish':  
            break        
        buy_dict = {}
        myfile = open('database.txt' ,'wt')
        for i in range(len(PRODUCTS)):
            if i < (len(PRODUCTS)-1):
                buy_dict['code'] = PRODUCTS[i]['code']
                buy_dict['name'] = PRODUCTS[i]['name']
                buy_dict['price'] = PRODUCTS[i]['price']
                buy_dict['count'] = PRODUCTS[i]['count']
                myfile.write(str(buy_dict['code']))
                myfile.write(',')
                myfile.write(buy_dict['name'])
                myfile.write(',')
                myfile.write(str(buy_dict['price']))
                myfile.write(',')
                myfile.write(str(buy_dict['count']))
            elif i == (len(PRODUCTS)-1):
                buy_dict['code'] = PRODUCTS[i]['code']
                buy_dict['name'] = PRODUCTS[i]['name']
                buy_dict['price'] = PRODUCTS[i]['price']
                buy_dict['count'] = PRODUCTS[i]['count']
                myfile.write(str(buy_dict['code']))
                myfile.write(',')
                myfile.write(buy_dict['name'])
                myfile.write(',')
                myfile.write(str(buy_dict['price']))
                myfile.write(',')
                myfile.write(str(buy_dict['count']))
            if i < (len(PRODUCTS)-1) :
                myfile.write('\n')              
                
def load_bill():
    buy_dict = {}
    myfile = open('bill.txt' ,'wt')
    Sum = 0
    for i in range(len(Bill)):
        if i < (len(Bill)-1):
            buy_dict['code'] = Bill[i]['code']
            buy_dict['name'] = Bill[i]['name']
            print('name product ' , buy_dict['name'])
            buy_dict['price'] = Bill[i]['price']
            print('price product ' , buy_dict['price'])
            buy_dict['count'] = Bill[i]['count']
            Sum = Sum + (int(buy_dict['price']) * int(buy_dict['count']))
            myfile.write(str(buy_dict['code']))
            myfile.write(',')
            myfile.write(buy_dict['name'])
            myfile.write(',')
            myfile.write(str(buy_dict['price']))
            myfile.write(',')
            myfile.write(str(buy_dict['count']))
        elif i == (len(Bill)-1):
            buy_dict['code'] = Bill[i]['code']
            buy_dict['name'] = Bill[i]['name']
            print('name product ' , buy_dict['name'])
            buy_dict['price'] = Bill[i]['price']
            print('price product ' , buy_dict['price'])
            buy_dict['count'] = Bill[i]['count']
            Sum = Sum + (int(buy_dict['price']) * int(buy_dict['count']))
            myfile.write(str(buy_dict['code']))
            myfile.write(',')
            myfile.write(buy_dict['name'])
            myfile.write(',')
            myfile.write(str(buy_dict['price']))
            myfile.write(',')
            myfile.write(str(buy_dict['count']))
        if i < (len(Bill)-1) :
            myfile.write('\n')     
    print('sum of price: ' , Sum)

Bill_file = []

def show_bill():
    bill_file= open('bill.txt' , 'r')
    data = bill_file.read()
    bill_list = data.split('\n')
    for i in range(len(bill_list)):
        product_info= bill_list[i].split(',')
        mydict = {}
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        Bill_file.append(mydict)
    for i in range(len(Bill_file)):
        print(Bill_file[i])

def Search_name():
    name_product = input("enter name product:")
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name'] == name_product:
            print(PRODUCTS[i]['code'])
            print(PRODUCTS[i]['name'])
            print(PRODUCTS[i]['price'])
            print(PRODUCTS[i]['count'])

def Qr_code():
    for i in range(len(PRODUCTS)):
        img = qrcode.make(str(PRODUCTS[i]))
        img.save('image' + str(i) + '.png')
    

load()
f = Figlet(font='standard')
print (f.renderText('Sajedeh Store'))

show_menue()
choice = int(input("pleas choose a number :"))
if choice == 1 :
    add_product()
elif choice == 2:
    edit_product()
    show_list()
elif choice == 3:
    Del_product()
elif choice == 4:
    Search_name()
elif choice == 5 :
    show_list()
elif choice == 6:
    buy_pro()
    load_bill()
elif choice == 7:
    Qr_code()
    # show_bill()
    # exit()
