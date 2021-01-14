from random import randint
#guss the no game 

def game():
    answer= randint(1,10)
    while True:
        try:        
            guess= int(input("Guess the number : "))
            if 0<guess<11:
                if guess==answer:
                    print('you are genious!!')
                    break
        except ValueError:
            print("please guess the number between 1 to 10")
        else:
            print("Keep trying")
            continue
        finally:
            print("Thank you !!!!")  
         