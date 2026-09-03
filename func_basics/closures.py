def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

square = chaicoder(2) # it pass the actual function refence with num = 2 referneces
cube = chaicoder(3)# it pass the actual function refence with num = 3 reference

print(square(4)) #it actually execute the actual function with x = 2 reference
print(cube(4)) # it actually execute the actual function with x = 3 reference