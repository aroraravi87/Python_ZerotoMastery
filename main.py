import sys
from pythonscripts import email_Send,passwordchecker

if __name__=='__main__':
#calling method
    #email_Send.send()
   sys.exit(passwordchecker.password_checker_main(sys.argv[1:]))


