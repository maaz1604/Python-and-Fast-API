day = str(input("Please enter today day: \n"))
age = int(input("Now, please enter your age: \n"))

price = 12 if age >=18 else 8

if(day=='Wednesday'):
    price -= 2

if(day=='Wednesday'):
    print('Hooray! wednesday bonzay $2 discount')
    print('Your total price is $',price)
    
else:
    print('Your total price is $',price)