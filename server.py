import socket
serv=socket.socket()
print('Server Socket Created')
serv.bind(('localhost',9999))
serv.listen(3)
print('Waiting for the connections ...')

while True:
    cli,addr=serv.accept()
    name=cli.recv(1024).decode()
    print('connected with ',addr,name)
    cli.send(bytes('Welcome to Server','utf-8'))
    cli.close()
