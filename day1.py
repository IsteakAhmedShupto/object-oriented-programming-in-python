# Classes and Instances

# Method =>  A function that is associated with a class
# Instances => Class is basically a blueprint for creating instances and for this example, each unique employee that we create using our employee class will be an instance of that class

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    def fullName(self):
        return f'{self.first} {self.last}'
        
emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Isteak','Shupto',60000)

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last  = 'Schafer'
# emp_1.email = 'Corey.Scafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Isteak'
# emp_2.last  = 'Shupto'
# emp_2.email = 'Isteak.Shupto@company.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullName())
# print(emp_2.fullName())

# Calling the class and passing Instances
print(Employee.fullName(emp_1))
print(Employee.fullName(emp_2))