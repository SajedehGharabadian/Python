
def sum_complex(x,y):
    result = {}
    result['r'] = x['r'] + y['r']
    result['Im'] = x['Im'] + y['Im']
    return result

def sub_complex(x,y):
    result = {}
    result['r'] = x['r'] - y['r']
    result['Im'] = x['Im'] - y['Im']
    return result

def mul_complex(x,y):
    result = {}
    result['r'] = x['r']*y['r'] - x['Im']*y['Im']
    result['Im'] = x['Im']*y['r'] + x['r']*y['Im']
    return result

def show(x):
    print(x['r'] , '+' , '(', x['Im'],')' , 'i')


real = int(input('enter real num:'))
imaginary = int(input('enter imaginary num:'))
a = {'r' : real , 'Im' : imaginary}

real = int(input('enter real num:'))
imaginary = int(input('enter imaginary num:'))
b = {'r' : real , 'Im' : imaginary}

c = sum_complex(a,b)
show(c)

d = sub_complex(a,b)
show(d)

e = mul_complex(a,b)
show(e)
