import socket

class ClientSocket:
    
    def __init__(self,server_ip,port,file_flag,file_name):
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.port = port
        self.server_ip = server_ip
        self.file_flag = file_flag

    def connect_to_server(self):
        self.client_socket.connect((self.server_ip,self.port))
        if file_flag == 1:
            f = open(file_name,'wb')
            l = self.client_socket.recv(1024)
            while l:
                print('receiving file...')
                f.write(l)
                l = self.client_socket.recv(1024)
            print('File received !')
            f.close()
        elif file_flag == 0:
            f = open(file_name,'rb')
            l = f.read(1024)
            while l:
                print('sending file ...')
                self.client_socket.send(l)
                l = f.read(1024)
            print('File sent ! whooa !')
            f.close()        

server_ip = raw_input('Enter the ip(ipv4) of the server to which you want to connect : ')
port = input('Enter the port number : ')
file_flag = input('If you want to receive a file enter 1, if you want to send a file enter 0 : ')

if file_flag == 1:
    file_name = raw_input('Enter the name which you want to give to receiving file : ')
elif file_flag == 0:
    file_name = raw_input('Enter the name of the file you want to send : ')

a = ClientSocket(server_ip,port,file_flag,file_name)
a.connect_to_server()
