class InheritMain:
    def Sign_In(self):
        print("User Logged In")


class User1(InheritMain):
    # Initalized Methods
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")


class User2(InheritMain):
    # Initalized Methods
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")


class User3(InheritMain):
    # Initalized Methods
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")


user1 = User1('user1', '20')
print('##################')
user1.Sign_In()
user1.display()

user2 = User2('user2', '40')
print('##################')
user2.Sign_In()
user2.display()

user3 = User3('user3', '50')
print('##################')
user3.Sign_In()
user3.display()
