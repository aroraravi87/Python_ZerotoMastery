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
            
        ''' 
        Cats are smarter then dogs
        '''   
def check_textString():
    try:
        line = input("Enter the string input : ")

        matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I) 
               
        if matchObj:
            print ("matchObj.group() :", matchObj.group())
            print ("matchObj.group(1) :", matchObj.group(1))
            print ("matchObj.group(2) :", matchObj.group(2))
        else:
            print("No Match!!!")
    except:
        print('Input string is not in correct format !!')


        ''' 
        Cats are smarter then dogs
        '''   
def check_SearchString():
    try:
        line = 'Cats are smarter then dogs'

        matchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I) 
               
        if matchObj:
            print ("matchObj.group() :", matchObj.group())
            print ("matchObj.group(1) :", matchObj.group(1))
            print ("matchObj.group(2) :", matchObj.group(2))
        else:
            print("No Match!!!")
    except:
        print('Input string is not in correct format !!')

check_SearchString()
