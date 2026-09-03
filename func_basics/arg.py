def sumAll(*args):
    return sum(args)

print(sumAll(1,5))
print(sumAll(5,7,9,4,6))

#kwargs

def any_args(name,power):
    print('Nmae: ',name,' Power: ',power)
    
any_args(name='Shaktiman',power='Lazer eye')

def print_kwargs(**kwargs):
    for key,val in kwargs.items():
        print(f"{key}:{val}")
        
print_kwargs(name = 'Power Ranger',power='Dinothunder')
print_kwargs(name='PowerRanger Jungle Fury',power='Beast Launch',enemy = 'Aliens')
