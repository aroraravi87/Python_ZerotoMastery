#python testing
def addition(num1, num2):
    try:
        if num1 and num2:
            return int(num1) + int(num2)
        else:
            print('please enter number')
    except ValueError as err:
        raise err

def multiply(num=0):
    try:
        if num:
            return int(num) * 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err

def divide(num1,num2):
    try:
        if num1 and num2:
            return int(num1) / int(num2)
        else:
            print('please enter number')
    except ValueError as err:
        raise err
