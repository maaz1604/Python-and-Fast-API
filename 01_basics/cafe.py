order_size = str(input('Please specify your coffee size: \n'))
extra_shot_str = bool(input('If you want extra shot, please type yes, otherwise type no \n'))

if(extra_shot_str == 'yes'):
    extra_shot = True
    
if(extra_shot_str == 'no'):
    extra_shot = False

if(extra_shot):
    coffee = order_size + ' coffee with an extra shot'
    
else:
    coffee = order_size + ' coffee'
    
print(coffee)