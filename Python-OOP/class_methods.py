# Object oriented programming
class Players:
    # class level attributes
    membership = True
    #Initalized Methods
    def __init__(self, name, age):
        if(Players.membership):
            self.name = name  # attributes
            self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

    def attack(self):
        print('attach called')

#class methods

    @classmethod
    def class_methodcalled(abc,num1,num2):
        return abc('classmethod',num1+num2);

#static methods
    @staticmethod
    def static_methodcalled(num1,num2):
        return num1+num2;

player1 = Players('James', '20')
print('##################')
player1.display()

player2 = Players('Tim', '30')

print('##################')
player2.display()


#called class method
player3=player1.class_methodcalled(30,20)
print(f"Age recalculated is {player3.age}")

#called static method
print(player1.static_methodcalled(10,20))

