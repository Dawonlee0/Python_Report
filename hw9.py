# 개념확인과제

class Rectangle:
    def __init__(self, h1, w1, h2, w2):
        self.h1 = h1
        self.w1 = w1
        self.h2 = h2
        self.w2 = w2

    def show(self):
        print(f'좌측 상단 꼭지점은 ({self.h1},{self.w1})이고 우측 상단 꼭지점이 ({self.h2},{self.w2})인 사각형 입니다.')

    def getWidth(self):
        self.w0 = self.w2 - self.w1

    def getHeight(self):
        self.h0 = self.h2 - self.h1

    def getArea(self):
        self.getWidth()
        self.getHeight()
        self.area = self.h0 * self.w0
        return self.area
    
    def getPerimeter(self):
        self.getWidth()
        self.getHeight()
        self.round = (self.w0 * 2) + (self.h0 * 2)
        return self.round

r1 = Rectangle(5,5,20,10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'넓이는 {a}, 둘레는 {p}')

