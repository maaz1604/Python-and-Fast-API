chai = 'Masala Chai'

slice_chai = chai[0:6]

print(slice_chai)


# string to list by using split 
chai_01 = "Lemon, Ginger, Masala, Mint"

print(chai_01.split(", "))

# we can use placeholder inside string in python 
# and use format option to use variable inside it.

chai_type ="Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)

print(order.format(quantity, chai_type))

# list to string by using 
car_varirty = ["Hyundai", "Toyota", "Marcedes", "Buggati", "Vellfire", "Tata"]
cars = str.join(', ',car_varirty)
print(cars)

hero = 'Super\nman'
print(hero)

hero1 = r'Super\nMan'
print(hero1)