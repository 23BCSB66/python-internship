import math

class Circle:
    def __init__(my, x, y, radius):
        my.x = x
        my.y = y
        my.radius = radius

    def get_area(my):
        return math.pi * (my.radius ** 2)

    def get_perimeter(my):
        return 2 * math.pi * my.radius

    def get_circumference(my):
        return my.get_perimeter()  

circle = Circle(int(input("Enter x-coordinate: ")),int(input("Enter y-coordinate: ")),int(input("Enter Radius: ")))
print(f"Area: {circle.get_area()}")
print(f"Perimeter: {circle.get_perimeter()}")
print(f"Circumference: {circle.get_circumference()}")
