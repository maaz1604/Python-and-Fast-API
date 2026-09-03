def even_generator(linit):
     for i in range(2,linit+1,2):
         yield i
     
print(even_generator(16))

for num in even_generator(10):
    print(num)
    