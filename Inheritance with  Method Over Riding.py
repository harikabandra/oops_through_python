class Animal:
    def sound(self):
        print("Animals make sounds")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

cat = Cat()
cat.sound()