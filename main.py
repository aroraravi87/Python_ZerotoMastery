#built in module.
from random import random
import sys


#Many way to import the package into main class.
#Custom build module
import pythonmodules.utilityhelper.utility
#way 1
from pythonmodules.utilityhelper.utility import multiply
#way 2
from pythonmodules.utilityhelper import utility
#way 3
from pythonmodules.shopping.shoppingcart import buy

from pythonmodules.guessnumbergame.guessnumber import game

if __name__ == "__main__":
    # print(pythonmodules.utilityhelper.utility.addition(10,20))
    # print(multiply(10, 10))
    # print(utility.divide(20, 10))
    # print(pythonmodules.shopping.shoppingcart.buy('Orange'))
    # print(buy('Apple'))

    #Guess the number 
    game()

##print(dir(random))
# print(random.random())
# print(random.randint(1, 10))
# print(random.choices([1, 2, 3, 4, 5]))
# mylist = [1, 2, 3, 4]
# random.shuffle(mylist)
# print(mylist)

#System module

#print(dir(sys))

#print(sys.argv)




