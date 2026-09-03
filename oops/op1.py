class Car:
    def __init__(self,userbrand,usermodel):
        self.brand = userbrand
        self.model = usermodel
        
    def fullName(self):
        return f'{self.brand} {self.model}'
    
    @staticmethod
    def general_description():
        return 'It is a means of Transport'
    
    
class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,batterysize):
        super().__init__(usermodel,userbrand)
        self.batterysize=batterysize
        
    def fname_with_baterry(self):
        return f'{self.fullName()} {self.batterysize}'
        
tesla = ElectricCar('Tesla','Model S','85kwh')
# print(tesla.fname_with_baterry())
        
my_car = Car('Mahindra','XUV-56')
# print(my_car.brand)
# print(my_car.fullName())

# print(my_car.general_description())

# print(Car.general_description())

class MyMeta(type):
    # This method belongs to the class object itself
    def strictly_class_built(cls, data):
        return f"Processing {data} via Metaclass."

class MyClass(metaclass=MyMeta):
    pass

# 1. Calling via Class Name (Works)
print(MyClass.strictly_class_built("hello"))  # Output: Processing hello via Metaclass.

# 2. Calling via Instance (Fails immediately)
obj = MyClass()
# obj.strictly_class_built("hello")  # AttributeError: 'MyClass' object has no attribute...
