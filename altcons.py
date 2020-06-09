class Employee:
    no_of_leaves=12
    def __init__(self,name,salary,role):
        self.name=name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"the name is {self.name} , the salary is {self.salary} & the role is {self.role}"
    @classmethod
    def from_dash(cls,str):         #one liner
        return cls(*str.split("/"))

"""
    @classmethod
    def from_dash(cls, str):
        p = str.split("/")  # this will split str into list wherever / comes
        # print(p)
        return cls(p[0], p[1], p[2])
"""


harry=Employee("Harry",555,"student")
larry=Employee("larry",5855,"influencer")
nikhil=Employee.from_dash("Nikhil/454/coder")         #only one arguement so we need an alternative costructor for this
print(nikhil.name)
print(nikhil.salary)
print(nikhil.role)
