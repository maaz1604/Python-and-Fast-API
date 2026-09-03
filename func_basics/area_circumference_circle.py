import math

def circle(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area,circumference

print(circle(5))