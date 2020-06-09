"""class Dad:
    dance=1
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
print(harry.dance)
print(harry.is_play())
print(harry.isdance())"""

##########electronics pocket gadget phone###########
class Electronicdevice():
    def electricity(self):
        print(f"i work on electricity")
class Pocketdevice(Electronicdevice):
    def portability(self):
        print(f"You can take me anywhere in your pocket")
class Mobilephone(Pocketdevice):
    def iscall(self):
        print(f"you can make a call")

a=Electronicdevice()
b=Pocketdevice()
c=Mobilephone()
c.electricity()
c.portability()
c.iscall()


