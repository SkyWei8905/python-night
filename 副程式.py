'''
def Sum(x):
    a = 0
    for i in range(1,x+1):  
        print (i)

Sum(10)
'''




'''
def Sum(x):
    a = 0
    for i in range(1,x+1):
        a+=i
    return a

z = Sum(10)
print(z)
'''
'''
def mul(x):
    a = 1
    for i in range(1,x+1):
        a*=i
    return a

z = Sum(10)
print(z)
'''

'''
def printStr(name, title='瓜'):
    print(f'name={name}, title={title}')
    
    
def calc(w, h):
    return (w+h)*2, w*h    


print(printStr(('哈')))

y,z = calc(3, 4)
'''


'''
s = [(3, 4),(2, 4),(5,3)]

def calc(w, h):
    return w * h
def calcAll(conta, func):
    for r in conta:
        print(func(r[0], r[1]), end=' ')  #這是註解哦~
       
calcAll(s, calc)
'''

'''
def Sum(x):
    a = 0
    for i in range(1,x+1):
        a+=i
    return a

def mul(x):
    a = 1
    for i in range(1,x+1):
        a*=i
    return a

def calcAll(value, func):
    return func(value)


print(calcAll(10, Sum))
print(calcAll(10, mul))
'''

'''
def calc(w, *args):
    for arg in args:
        w = w * arg
    return w

y = calc(3, 4, 5, 6)
print(y)    
'''
def calc2(w, **kwargs):
    print (w, kwargs)

calc2('chris', a=1, b=2)















