from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, color='black') -> None:
        self.color = color

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color='gray') -> None:
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, height, width, color='blue') -> None:
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3, color='green') -> None:
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
if __name__ == "__main__":

    circle1 = Circle(8, 'purple')
    circle2 = Circle(3, "red")
    rectangle1 = Rectangle(2, 4, 'silver')
    rectangle2 = Rectangle(24, 48, 'yellow')
    triangle1 = Triangle(2, 3, 4, 'black')
    triangle2 = Triangle(3, 4, 6, 'brown')

    print(f"{circle1.calculate_area()}")
    print(f"{circle2.calculate_area()}")
    print(f"{circle1.calculate_perimeter()}")
    print(f"{rectangle1.calculate_area()}")
    print(f"{rectangle2.calculate_area()}")
    print(f"{rectangle2.calculate_perimeter()}")
    print(f"{triangle1.calculate_area()}")
    print(f"{triangle2.calculate_area()}")
    print(f"{triangle1.calculate_perimeter()}")

    shapes = [circle1, circle2, rectangle1, rectangle2, triangle1, triangle2]

    for shape in shapes:
        print(f"Perimeter: {circle1.calculate_perimeter()}")
        print(f"Area: {circle2.calculate_area()}")
        print(f"Perimeter: {rectangle1.calculate_perimeter()}")
        print(f"Area: {triangle1.calculate_area()}")
        print(f"Perimeter: {triangle2.calculate_perimeter()}")
