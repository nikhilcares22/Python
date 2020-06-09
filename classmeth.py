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

harry=Employee("Harry",555,"student")
larry=Employee("larry",5855,"influencer")
harry.change_of_leaves(21)
#print(harry.no_of_leaves)       #it'll change no_of_leaves of the class without self in arguements
#print(Employee.no_of_leaves)
#print(larry.no_of_leaves)
harry.print_good("Harry")