class Employee:
    employee_id = 101
    name = "Harika"
    basic_salary = 80000
    
    def calculate_salary(self):
        hra = 20 / 100 * self.basic_salary
        da = 10 / 100 * self.basic_salary
        total = self.basic_salary + hra + da
        print("Total Salary:",total)
        
    def display(self):
        print("employee id:",self.employee_id)
        print("employee name:",self.name)
        print("basic salary:",self.basic_salary)
        self.calculate_salary()

E = Employee()

#E.calculate_salary()
E.display()