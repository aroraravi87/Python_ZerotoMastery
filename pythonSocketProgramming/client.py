import socket
def client_program():

    client_Socket=socket.socket()
    host=socket.gethostname()
    port=5000

    client_Socket.connect((host,port))
    
    message=input("-> ")
    while message.lower().strip()!='bye':
        client_Socket.send(message.encode())
        data=client_Socket.recv(1024).decode()
        print("Received from server : "+data)
        message=input("-> ")
    client_Socket.close()

if __name__=='__main__':
    client_program()