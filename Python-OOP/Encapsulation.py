Object oriented programming

Encapsulation.


class Players:

    # Initalized Methods
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")


player1 = Players('James', '20')
print('##################')
player1.display()

# Abstraction


class Abstraction:

    # Initalized Methods
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")


player1 = Abstraction('James', '20')
print('##################')
player1.display()


# abstract count method logic when applied on tuple.
print(f"count of 1 is {(1,2,4,1,2,1).count(1)}")
