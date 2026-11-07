class Student:
    name = "Karthika"
    age = 18
    
    def read(self):
        print("Reading")
    def write(self):
        print("Writing")
        
s1 = Student()
s2 = Student()
s3 = Student()

print("Name:",s1.name)
print("age: ",s1.age)
s1.read()
s1.write()