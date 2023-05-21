# from decimal import  Decimal

class Figure:
    def __init__(self, no_of_sides):
        self.n = no_of_sides                         # кількість сторін
        self.sides = [0 for i in range(no_of_sides)] # розміри сторін

    def input_sides(self):
        # розмір кожної зі сторін
        self.sides = [float(input("Введіть сторону фігури "+ str(i + 1) + " : ")) for i in range(self.n)]


    def disp_sides(self):
        # виводить на екран
        for i in range(self.n):
            print("Сторона", i + 1, ' - ', self.sides[i])


class Triangle(Figure):
    def __init__(self):
        Figure.__init__(self, 3)

    def perimetr_triangle(self):
        a, b, c = self.sides
        per = a + b + c
        print("Периметр трикутника: ", per)


    def find_area_triangle(self):
        a, b, c =self.sides
        half_per = (a + b + c)/2
        area = (half_per *(half_per - a)* (half_per - b)* (half_per - c) ** 0,5)
        print("Площа трикутника : ", area)

triangle = Triangle()
triangle.input_sides()
triangle.disp_sides()
triangle.perimetr_triangle()
triangle.find_area_triangle()

class Rectangle(Figure):
    def __int__(self):
        Figure.__init__(self, 4)

    def perimetr_rect(self):
        a, b, c, d = self.sides
        perim = a + b + c + d
        print("Периметр прямокутника: ", perim)


    def find_area_rect(self):
        a, b, c, d = self.sides
        area_rect = a * b
        print("Площа прямокутника : ", area_rect)

rectangle = Rectangle(4)
rectangle.input_sides()
rectangle.disp_sides()
rectangle.perimetr_rect()
rectangle.find_area_rect()

# Rectangle = Square


