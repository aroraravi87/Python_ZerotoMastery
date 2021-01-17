#Regular expression

import re

def checkstr():
    pattern = re.compile('this')
    string = 'This is my first program with this regular expression  !!!'
    #output = pattern.search(string)
    output = pattern.findall(string)
    #output=pattern.match(string)
    #output=pattern.fullmatch(string)
    return output

def checkstr_regex():
    pattern = re.compile(r"([a-zA-Z]).([a])")
    string = 'This is my first program with this regular expression  !!!'
    output = pattern.search(string)
    #output = pattern.findall(string)
    #output=pattern.match(string)
    #output=pattern.fullmatch(string)
    return output.group(2)

def check_emailexp():
        try:
            pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
            string = input("Enter the email address : ")
            output = pattern.search(string)
            if output:
                print("Email address is valid")
            else:
                print("Email address is Invalid")
        except:
            print('Incorrect string enter !!')

def check_passwordexp():
        try:
            pattern = re.compile(r"[a-zA-Z0-9@#$%]{8,}\d")
            password = input("Enter the password : ")
            output = pattern.fullmatch(password)
            if output:
                print("Valid password")
            else:
                print("Invalid password")
        except:
            print('Incorrect input entered !!')
