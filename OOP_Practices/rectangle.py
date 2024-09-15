'''

Create a class Rectangle that has properties for width and height and methods to calculate the area and perimeter.
'''

class Rectangle():

    def __init__(self, width:float, height:float):

        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.height * self.width

        return f"Area of rectangle: {area}"

    def calculate_Perimeter(self):

        perimeter = 2*(self.width + self.height)
        return f"Perimeter of rectangle :{perimeter}"


example1 = Rectangle(3.14,2.14)
print(example1.calculate_area())
print(example1.calculate_Perimeter())