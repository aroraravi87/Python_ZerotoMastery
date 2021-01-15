from translate import Translator

def readfilecontent():
    try:
        my_file =open('pythonfileIO\hello.txt')
        print(my_file.read())
        my_file.seek(0)
        print(my_file.read())
    
        #way2 Read
        with open('pythonfileIO\hello.txt') as my_file:
           print(my_file.readlines())

    except:
        print("Invalid file path or read error !!")
    finally:
          my_file.close()

def writefilecontent():
    try:
        #write new content and clear all 
        with open('pythonfileIO\hello.txt',mode='w') as my_file:
           print(my_file.write("New content added !!!"))
        #append new content and retain existing one

        with open('pythonfileIO\hello.txt',mode='a') as my_file:
           print(my_file.write("\nI am learning now file modes to modify file !!!"))
        
        # write will create new file and add content
        with open('pythonfileIO\sad.txt',mode='w') as my_file:
           print(my_file.write("\nNew content added into new file!!!"))
        

    except FileNotFoundError as err:
        print("Invalid file path or file not exist !!")
        raise err
    except IOError as err:
        print("IO error")
        raise err

def translatefilecontent():
    try:
        translater=Translator(to_lang="ja")
        #read  content and clear all 
        with open('pythonfileIO\hello.txt',mode='r') as my_file:
           content=my_file.read()
           translation=translater.translate(content)
           print(translation)
            # # write will create new file and add content
        with open('pythonfileIO\hello-translate.txt',mode='w') as my_file1:
            #print(type(translation))
            my_file1.write(translation)
        

    except FileNotFoundError as err:
        print("Invalid file path or file not exist !!")
        raise err
    except IOError as err:
        print("IO error")
        raise err
