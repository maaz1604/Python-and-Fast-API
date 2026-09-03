numbers = [1,-2,3,-5,8,-7,-54,25,78]

even_sum = 0

for num in numbers:
    if(num%2==0 and num>0):
        even_sum += num
        
print(even_sum)
even_sum = 0;

n = int(input('Please type a positive integer number: \n'))

for i in range(1,n+1):
    if(i%2==0):
        even_sum += i
        
print('Sum of even number is: ',even_sum)