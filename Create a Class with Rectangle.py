class Rectangle:
    def area(self, l, b):
        print("Aera:",l * b)
        
    def perimeter(self, l, b):
        print("Perimeter:",2 * (l + b))

l = int(input("Enter length - "))
b = int(input("Enter breadth - "))

rec = Rectangle()

rec.area(l, b)
rec.perimeter(l, b)