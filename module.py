#built in module.
from random import random
import sys

#debugger 
import pdb

#import pyjokes

#collection module
from collections import Counter,OrderedDict,defaultdict

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
    # game()
    
    #print the pyjokes
   # joke=pyjokes.get_joke('en','neutral')
    #print(f"Pyjoke is : ",joke)
    def sum(num1,num2):
        pdb.set_trace()
        return num1+num2

    print(sum(4,5))


    #collection module

    list = [1, 2, 1, 3, 4, 5, 6, 4, 6, 7]
    
    print(Counter(list))

    #default dict

    dict = defaultdict(int, {'a': 1, 'b': 2})
    
    dict1 = defaultdict(lambda:'Does not exists',{'a': 1, 'b': 2})
    print(dict['c'])
    print(dict1['c'])

    #OrderDict

    dict3 = OrderedDict({'c': 1})
    dict3['a'] = 2
    dict3['b']=3

    dict4 = OrderedDict({'c': 1})
    dict4['b'] = 3
    dict4['a']=2
    
    print(dict3==dict4)

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





