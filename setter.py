class Emp:
    def __init__(self,f,l):
        self.f=f
        self.l=l
        #self.email=f"{f}.{l}@gmail.com"
    def exp(self):
        return f"The employee is {self.f} {self.l}"
    @property
    def email(self):            #can be called as an object
        if self.f==None or self.l ==None:
            return f"email is not set"
        return f"{self.f}.{self.l}@gmail.com"
    @email.setter
    def email(self,string):
        print("SETTING NOW")
        x=string.split("@")
        self.f=x[0].split(".")[0]
        self.l=x[0].split(".")[1]
    @email.deleter
    def email(self):
        self.f=None
        self.l=None

a=Emp("Nikhil","Sharma")
print(a.email)
a.f="Mohan"
#print(a.email)     #it will not change as constructor ran in runtime when we made the instance
a.email="this.that@gmail.com"
print(a.f)
print(a.l)
print(a.email)
del a.email
print(a.email)
a.email="nikhil.cares22@gmail.com"
print(a.email)