class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        return Circle.pi*self.radius**2

    def getCircumference(self):
        return 2*Circle.pi*self.radius


st= Circle(5)
print(st.getArea())
print(st.getCircumference())