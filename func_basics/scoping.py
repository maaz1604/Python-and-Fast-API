username = 'Ferrari'

def func():
    username = 'G-Wagon'
    
print(username)

x = 9

def func3(u):
    z = u + x
    return z

result = func3(56)
print(result)

def fn():
    x = 98
    def f2():
        print(x)
    return f2

ans = fn()
ans()
