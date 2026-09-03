number = int(input('Please enter a number: '))

is_prime = True

if number>1:
    for i in range(2,number):
        if (number%i) == 0:
            is_prime=False
            break
        
if(is_prime and number>1):
    print('The number is Prime.')
else:
    print('The number is not Prime.')