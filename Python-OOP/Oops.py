class Players:
    valid=True

    def __init__(self,name,age):
        if(Players.valid):
            self.name=name
            self.age=age
    
           
    def display(self):
        print(f"name is {self.name} and age is {self.age} and membership status {self.valid}")
        print("name is {}".format(self.name))
  
    def attack(self):
        print(f"Action taken by {self.name}")
    

player1=Players('Smith','20')
player1.display()
print("Membership status is {}".format(player1.__class__.valid))

player2=Players("Adam",20)
player2.attack()