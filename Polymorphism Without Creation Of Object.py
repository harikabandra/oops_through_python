class Dog:
    def sound(self):
        print("Dog says Woof")

class Cat:
    def sound(self):
        print("Cat says Meow")

def animal_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)