class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
    def print_details(self):
        return f"His name is {self.name}, his role is {self.role} and his salary is {self.salary}"
class Player:
    no_of_game=5
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def print_details(self):
        return f"His name is {self.name} and his games are {self.game}"
class CoolProgrammer(Employee,Player):      #constructor depends on the order here
    def print(self):
        return f"he is cool"


nikhil=CoolProgrammer("nikhil","Programmer",8989)
print(nikhil.print_details())        #if Employee is in first
print(nikhil.print())
"""nikhil=CoolProgrammer("Nikhil",{"Cricket","Football"})
print(nikhil.print_details())"""        #if Player is in first

