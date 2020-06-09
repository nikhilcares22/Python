class Dad:
    dance=1
    _a=12       #protected
    __b=14      #private
    def isdance(self):
        return f"yes i can dance {self.dance}"
class Son(Dad):
    basketball=1
    def is_play(self):
        return f"yes i can play basketball"

class Grandson(Son):
    dance=10
    def isdance(self):
        return f"yes i can dance {self.dance}"

darry=Dad()
larry=Son()
harry=Grandson()
print(harry._a)         #can be accessed out of the class by derived class
print(darry._Dad__b)    #name angling
print(larry._Dad__b)
print(harry._Dad__b)


