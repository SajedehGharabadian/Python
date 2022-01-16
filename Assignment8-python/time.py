
def sum(x,y):
    result = {}
    result['h'] = x['h'] + y['h']
    result['m'] = x['m'] + y['m']
    result['s'] = x['s'] + y['s']
    if result['s'] >=  60:
        result['s'] = result['s'] - 60
        result['m'] += 1

    elif result['m'] >= 60:
        result['m'] -= 60
        result['h'] += 1
    return result

def sub(x,y):
    result = {}
    if x['h'] > y['h']:
        result['s'] = x['s'] - y['s']
        result['m'] = x['m'] - y['m']
        result['h'] = x['h'] - y['h']
        if result['s'] < 0:
            result['s'] = result['s'] + 60
            result['m'] -= 1
        if result['m'] < 0:
            result['m'] += 60
            result['h'] -= 1
        result['h'] = x['h'] - y['h']
    else:
        result['s'] = y['s'] - x['s']
        result['m'] = y['m'] - x['m']
        result['h'] = y['h'] - x['h']
        if result['s'] < 0:
            result['s'] = result['s'] + 60
            result['m'] = result['m'] - 1
        if result['m'] < 0:
            result['m'] = result['m'] + 60
            result['h'] -= 1
    return result

def time_tosecond(x):
    result = x['h']*3600  + x['m']*60 + x['s']
    return result

def second_totime():
    result = {}
    x = int(input('enter second:'))
    result['h'] = str(x // 3600) 
    remain = x % 3600
    result['m'] = str(remain // 60)
    result['s'] = remain % 60
    return result

def show(x):
    print(x['h'] , ':' , x['m'] , ':' , x['s'])

hour = int(input('enter hour:'))
minute = int(input('enter minute:'))
second = int(input('enter second:'))
t1 = {'h':hour , 'm':minute , 's':second}

hour = int(input('enter hour:'))
minute = int(input('enter minute:'))
second = int(input('enter second:'))
t2 = {'h':hour , 'm':minute , 's':second}

t3 = sum(t1,t2)
show(t3)

t4 = sub(t1,t2)
show(t4)

t5 = time_tosecond(t1)
print(t5)

t6 = second_totime()
show(t6)