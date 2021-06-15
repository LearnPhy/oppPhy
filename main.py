from geometry.rectangle import Rectangle
from geometry.triangle import Triangle

rectangle1 = Rectangle(8, 4)
print(rectangle1.info())

print(rectangle1.calculate_area())

print('---------------====================-------------------')

triangle1 = Triangle(8, 4, "Triangle")
print(triangle1.info())

print(f'The Area of the {triangle1.s} is {triangle1.calculate_area()}')
