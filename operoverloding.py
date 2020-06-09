class Employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def __str__(self):
        return f"The name is {self.name}, salary is {self.salary} and role is {self.role}"
    def __repr__(self):
        return f"Employee('{self.name}','{self.salary}',{self.role})"
    def __add__(self, other):
        return self.salary + other.salary
    def __floordiv__(self, other):
        return self.salary//other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __contains__(self, item):
        return item in self.name
    
a=Employee("Nikhil",455,"Programmer")
b=Employee("Rohan",45,"Sweeper")
"""print(a+b)
print(a//b)
print(a/b)"""
"""print(a)
print(b)
print(repr(b))
print(repr(a))"""
#print('N'in a)


