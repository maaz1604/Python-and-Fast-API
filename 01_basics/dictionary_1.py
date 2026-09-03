state_capital = {'Bihar':'Patna', 'jharkhand':'ranchi', 'assam':'tripura', 'nagaland':'kohima'}

for state in state_capital:
    print(state)
    
for state,capital in state_capital.items():
    print(state, capital)
    
tea_shop = {
    "chai" : {
        "Masala":"Spicy",
        "Ginger":"Zesty"
    },
    "tea" : {
        "green" : "mild",
        "black":"strong"
    }
}   

print(tea_shop["chai"])
print(tea_shop["tea"])

sq_nums = {x:x**2 for x in range(10)}
print(sq_nums)

for key,val in sq_nums.items():
    print(key, "->" ,val)
    
sq_nums.clear()
print(sq_nums)

# using list to form dictionary
keys = ['Buggati','cheron','mercedes','toyota']
default_value = 'red'

new_dict = dict.fromkeys(keys,default_value)
print(new_dict)