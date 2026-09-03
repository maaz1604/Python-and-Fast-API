def debug(func):
    def wrapper(*args,**kwargs):
       arg_value = ', '.join(str(arg) for arg in args)
       kwarg_value = ', '.join(f'{key} : {value}' for key,value in kwargs.items())
       print(f'calling: {func.__name__} with args {arg_value} and kwargs {kwarg_value}')
       return func(*args,**kwargs)
          
    return wrapper

@debug
def greet(name,greeting='Hello'):
    print(f'{greeting}, {name}')
    
greet('chai',greeting='Hi!')