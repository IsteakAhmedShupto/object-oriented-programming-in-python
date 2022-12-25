# Special (Magic/Dunder) Methods

class Employee:
    
    raise_amt = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first+"."+last+"@email.com"
        self.pay = pay
         
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay+self.raise_amt)
        
    def __repr__(self):
        return f"Employee ({self.first}, {self.last}, {self.pay})"
    
    def __str__(self):
        return f"{self.fullname}, {self.email}"    
    
    def __add__(self,other):
        return self.pay+other.pay
    
    def __len__(self):
        return len(self.fullname())    
        
emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Isteak","Shupto",60000)

print(emp_1+emp_2)
print(emp_1.__len__())

# print(emp_1.__repr__())        
# print(emp_1.__str__())  

# print(int.__add__(1,2))
# print(str.__add__('a','b'))