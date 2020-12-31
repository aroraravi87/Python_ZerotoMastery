class User:
    def Sign_In(self):
        print("User Logged In")


class Wizard(User):
    # Initalized Methods
    def __init__(self, name, power):
        self.name = name  # attributes
        self.power = power

    def shout(self):
        print(f"Name is {self.name} and power is {self.power}")
   

class Archer(User):
    # Initalized Methods
    def __init__(self, name, arrows):
        self.name = name  # attributes
        self.arrows = arrows

    def check_arrows(self):
        print(f"Arrows remaining {self.arrows}")

    def run(self):
        print(f"Ran method called.")


class Pacmen(Wizard,Archer):
   def __init__(self,name,power,arrows):
        Archer.__init__(self,name,arrows)
        Wizard.__init__(self,name,power)


pac = Pacmen('user1',20,100)
print('##################')
pac.shout()
print('##################')
pac.check_arrows()
print('##################')
pac.Sign_In()




