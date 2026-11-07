class shape:
    def area(self):
        print("area of shape")

class circle:
    def area(self):
        r = 5
        print("Circle area: ",3.14*r*r)

class rectangle:
    def area(self):
        l = 6
        b = 14
        print("Rectangle area: ",l*b)

class triangle:
    def area(self):
        base=21
        height=17
        print("Triangle area: ",0.5*base*height)

c=circle()
r=rectangle()
t=triangle()

c.area()
r.area()
t.area()