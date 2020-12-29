class User:
    def Sign_In(self):
        print("User Logged In")


class Wizard(User):
    # Initalized Methods
    def __init__(self, name, power):
        self.name = name  # attributes
        self.Power = power

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
   pass


pac = Pacmen('user1', '20')
print('##################')
pac.Sign_In()



