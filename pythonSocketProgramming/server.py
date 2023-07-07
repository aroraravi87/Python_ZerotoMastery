import socket

def server_Socket_program():

    server_socket=socket.socket()
    host=socket.gethostname()
    port=5000
    server_socket.bind((host,port))
    print(host)
    server_socket.listen(2)
    print(server_socket)
    conn,addr=server_socket.accept()
    print("connection from: "+ str(addr))
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print('From connected user: '+str(data))
        data =input('-> ')
        conn.send(data.encode())
    conn.close()

if __name__=='__main__':
    server_Socket_program()
    print("Server is up and running!!")