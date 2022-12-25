# class variables

class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last =last
        self.pay = pay
        self.email = first+"."+last+"@company.com"
        Employee.num_of_emps +=1
        
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay  = int(self.pay * self.raise_amount)
     
emp_1 = Employee("Corey","Scafer",50000)
emp_2 = Employee("Isteak","Shupto",60000)
 
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount
# Employee.raise_amount

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# Employee.raise_amount = 1.05

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount) 
print(emp_2.raise_amount)

print(Employee.num_of_emps)