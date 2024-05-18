class Rectangle:
    def __init__(self, x1, y1, x2, y2): # x1 < x2, y1 < y2
        self.__lt = (x1, y1)
        self.__rb = (x2, y2)

    def show(self):
        print(f'좌측 상단 꼭지점이 {self.__lt}이고 우측 하단 꼭지점이 {self.__rb}인 사각형입니다.', end ='')

    def getWidth(self):
        lt_x1 = int(self.__lt[0])
        rb_x2 = int(self.__rb[0])
        width = rb_x2 - lt_x1
        return width

    def getHeight(self):
        lt_y1 = int(self.__lt[1])
        rb_y2 = int(self.__rb[1])
        height = rb_y2 - lt_y1
        return height

    def getArea(self):
        area = self.getWidth() * self.getHeight()
        return area

    def getPerimeter(self):
        perimeter = 2 * (self.getWidth() + self.getHeight())
        return perimeter

# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
