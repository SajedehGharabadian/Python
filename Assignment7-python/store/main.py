from pyfiglet import Figlet



def show_menue():
    print("1- Add product")
    print("2- Edit product")
    print("3- Dlete Product")
    print("4- Search")
    print("5- Show List ")
    print("6- Buy")
    print("7- Exit")

products = []

def load():
    print('loading...')
    f = open('database.txt' , 'r')

    rows = f.read().split('\n')
    for i in range(len(rows)):
        info = rows[i].split(',')
        products.append({'id': int(info[0]) ,'name' : info[1] , 'price' : float(info[2]) ,  'count' : int(info[3])})
    
    f.close()
    print('Programm is ready to use!')

def add_product():
    id = int(input('please enter code:' ))
    name = input('please enter name: ')
    price = float(input('please enter price: '))
    count = int(input('please enter count: '))
    products.append({'id': id , 'name' : name , 'price' : price , 'count' : count})
    print('New products added successfully')

def show_edit_menue():
    print('1- name')
    print('2- price')
    print('3- count')
    print('4- end edit')

def edit_product():
    id = int(input('please enter product id: '))
    for i in range(len(products)):
        if id == products[i]['id']:
            while True:
                show_edit_menue()
                choice = int(input('please choose from edit menue'))

                if choice == 1:
                    products[i]['name'] = input('please enter new name:')
                elif choice == 2:
                    products[i]['price'] = float(input('please enter new price: '))
                elif choice == 3:
                    products[i]['count'] = int(input('please enter new count:'))
                elif choice == 4:
                    break
                else:
                    print('Value error')

def delete_product():
    id = int(input('please enter product id :'))
    for i in range(len(products)):
        if products[i]['id'] == id:
            products.pop(i)    #del products[i]
            print('Product removed!')
            break

def search_product():
    user_keyword = input('please enter id or name: ')
    for i in range(len(products)):
        if products[i]['name'] == user_keyword or str(products[i]['id']) == user_keyword:
            print(products[i])

def show_list():
    for i in range(len(products)):
        print(products[i]['id'] , '\t' , products[i]['name'] , '\t' , products[i]['price'] , '\t' , products[i]['count'] , '\t')

def buy_product():
    basket = []
    while True:
        id = int(input('please enrer product id:'))
        for i in range(len(products)):
            if products[i]['id'] == id:
                count = int(input('please enter count product:'))

                if products[i]['count'] >=  count :
                    basket.append({'name' : products[i]['name'] ,
                                'price' : products[i]['price'] ,
                                'count' : count})
                    products[i]['count'] -= count
                    print('product added to basket successfully!')
                else:
                    print('not exist!')
                    print('we have' , products[i]['count'] , 'from this product')
        choice = input('do you want to countinue? (Y/N)')
        if choice == 'n' or choice == 'N':
            break
    print(basket)
    
    total_price = 0
    for i in range(len(basket)):
        total_price += basket[i]['price']*basket[i]['count']
    print('total price is' , total_price )
    print('Thanks')

def save_and_exit():
    f = open('database.txt' , 'w')
    for i in range(len(products)):
        if i < (len(products)-1):
            row = str(products[i]['id']).format() + ',' + products[i]['name'] + ',' + str(products[i]['price']).format() + ',' + str(products[i]['count']).format() + '\n'
            f.write(row)
        if i == (len(products)-1) :
            row = str(products[i]['id']).format() + ',' + products[i]['name'] + ',' + str(products[i]['price']).format() + ',' + str(products[i]['count']).format()
            f.write(row)

    f.close()
    exit()

load()
f = Figlet(font='standard')
print (f.renderText('Sajedeh Store'))

while True:
    show_menue()
    choice = int(input("pleas choose a number :"))
    if choice == 1 :
        add_product()
    elif choice == 2:
        edit_product()
    elif choice == 3:
        delete_product()
    elif choice == 4:
        search_product()
    elif choice == 5 :
        show_list()
    elif choice == 6:
        buy_product()
    elif choice == 7:
        save_and_exit()
