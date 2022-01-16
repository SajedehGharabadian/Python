def sum(x,y):
    result = {}
    result['s'] = x['s']*y['m'] + y['s']*x['m']
    result['m'] = x['m']*y['m']
    return result



def mult(x,y):
    resulat ={}
    resulat['s'] = x['s']*y['s']
    resulat['m'] = x['m']*y['m']
    return resulat       #if print(result) this is not true evry where

def sub(x,y):
    result = {}
    result['s'] =  x['s']*y['m'] - y['s']*x['m']
    result['m'] = x['m'] * y['m']
    return result

def div(x,y):
    result = {}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']
    return result

def show(x):
    print(x['s'], '/' , x['m'])

numerator = int(input('enter numerator:'))
denominator = int(input('enter denominator:'))
a = {'s':numerator , 'm':denominator}

numerator = int(input('enter numerator:'))
denominator = int(input('enter denominator:'))
b = {'s':numerator , 'm':denominator}


c = mult(a,b)
show(c)
print(c)

d = sum(a,c)
show(d)
print(d)

e = sub(a,b)
show(e)
print(e)

f = div(a,b)
show(f)
print(f)