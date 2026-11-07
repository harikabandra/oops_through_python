class Sample:
    def __init__(self,name,age):
        self.name = name
        self.age=age
        
    def read(self):
        print("Name:",self.name)
        print("age:",self.age)
    
s1 = Sample("Harika",19)
s1.read()
    
s2 = Sample("Manasa",20)
s2.read()