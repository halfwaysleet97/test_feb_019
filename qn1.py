class SquareGeometry:
    def __init__(self,length):
        self.length=length

    def getArea(self):
        return self.length*self.length

    def getPerimeter(self):
        return 4*self.length


s=SquareGeometry(5)
print(s.getArea())
print(s.getPerimeter())