def ReadFile():
    try:
        myfile=open("pythonfileIO/sad.txt",'r')
        print(myfile.read())
        
        '''Way 2 read'''
        with open("pythonfileIO/hello.txt",'r') as my_file:
            print(my_file.read())

    except IOError as err:
        print("file read error!!")
        return err
    
    finally:
        my_file.close()
        myfile.close()


def WriteFile():
    try:
        myfile=open("pythonfileIO/sad.txt",'a')
        myfile.write("\nNew information ambeded again")
       
        '''Way 2 read'''
        with open("pythonfileIO/sad.txt",'r') as my_file:
            print(my_file.read())
       
    except IOError as err:
        print("file read error!!")
        return err
    
    finally:
        my_file.close()
        myfile.close()



        
'''ReadFile()'''
WriteFile()