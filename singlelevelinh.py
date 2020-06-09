class Employee:
    no_of_leaves=12
    def __init__(self,name,salary,role):
        self.name=name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"the name is {self.name} , the salary is {self.salary} & the role is {self.role}"
    @classmethod
    def change_of_leaves(cls,new_leaves):
        no_of_leaves=new_leaves
    @staticmethod
    def print_good(s):      #static method
        print(f"{s} is goood")
class programmer(Employee):
    def __init__(self,name,salary,role,languages):
        self.name= name
        self.salary =salary
        self.role = role
        self.languages = languages
    def print_it(self):
        return f"The programmer's name is {self.name}, his salary is {self.salary}, his role is {self.role} and he knows these laguages {self.languages}"
nikhil=programmer("Nikhil",555,"Programmer",["python","C++"])
print(nikhil.print_it())