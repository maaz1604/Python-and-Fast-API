city = ['New York', 'Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Pune', 'Hyderabad']
print(city[1:4])

city[1:2] = 'Lemon'
print(city)

city2 = ['New York', 'Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Pune', 'Hyderabad']
city[1:2] = ['Lemon']
print(city2)

for c in city2:
    print(c)
    
for c in city2:
    print(c,end='-')
   
print('\n') 
# List comprehension
squared_nums = [x**2 for x in range(10)]
print(squared_nums)