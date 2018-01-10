import socket

class ServerSocket:

    def __init__(self,port,file_flag,file_name):
        self.file_flag = file_flag
        self.file_name = file_name
        self.server_socket = socket.socket()
        try:
            self.server_socket.bind(('',port))
        except (TypeError, socket.error) as e:
            print('error occured : ', e)

    def  initiate_server(self):
        self.server_socket.listen(10)
        while True:
            c, addr = self.server_socket.accept()
            if self.file_flag == 0:
                f = open(file_name,'rb')
                l = f.read(1024)
                while l:
                    print('sending file...')
                    c.send(l)
                    l = f.read(1024)
                print('File Sent ! whooa !')
                f.close()
                c.close()
            elif self.file_flag == 1:
                f = open(file_name,'wb')
                l = c.recv(1024)
                while l:
                    print('receiving file ... ')
                    f.write(l)
                    l = c.recv(1024)
                print('File received !')
                f.close()
                c.close()

port = input('Enter the port on which you want to start the server : ')
file_flag = input('Enter 1 if you want to receive a file, 0 if you want to send a file : ')

if file_flag == 0:
    file_name = raw_input('Enter the file name you want to send : ')
elif file_flag == 1:
    file_name = raw_input('Enter the name you want to give to received file : ')

a = ServerSocket(port, file_flag,file_name)
a.initiate_server()
