# Python_ZerotoMastery

Learn Python from scratch. 

#Refer the below URl and command to setup the Flask server for web development.

https://flask.palletsprojects.com/en/1.1.x/quickstart/

Setup the virtual env.

    Create a project folder and a venv folder within:

    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv venv
    
    On Windows:

    $ py -3 -m venv venv
    
    If you needed to install virtualenv because you are using Python 2, use the following command instead:

    $ python2 -m virtualenv venv
    
    On Windows:

    .\Scripts\virtualenv.exe venv
   
    Activate the environment
    Before you work on your project, activate the corresponding environment:

        $ . venv/bin/activate
        On Windows:

        venv\Scripts\activate


Setup the flask server

    pip3 install flask

    IOS/Linux
        $ export FLASK_APP=server.py
        $ flask run

    Window-powershell/command prompt.
        cmd- set FLASK_APP=server.py
        powershell- $env:FLASK_APP = "server.py"
        $ python -m flask run or flask run.

    Enable the debug mode.
        cmd- set FLASK_ENV=development
        powershell- $env:FLASK_ENV="development"
        $ flask run


Note:
    Flask use jinja to evaluate the expression like {{4+5}}= 9
    #flask framework use for small application.
    #django framework  for buld complex application.