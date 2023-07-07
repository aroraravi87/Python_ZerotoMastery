def sum():
    try:
        return 1 + 'Name'
    except:
        print("Invalid type")
    else:
        print("thank you")
    finally:
        print("Finally method called at last")
#print(sum())


##################3

while True:
    try:
       value=int(input("What your age: "))
       10 / value
     #  raise Exception("incorrect value passed") #custom error passed.
    except ValueError:
        print("Please enter the number")
        continue
    except ZeroDivisionError:
        print("## Value should be greater than zero!!!")
        break
    else:
        print("## thank you !!!")
        break
    finally:
        print("## Finally method called at last")