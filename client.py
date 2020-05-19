import socket
cli=socket.socket()
cli.connect(('localhost',9999))
name=input('Enter the name of the user:')
cli.send(bytes(name,'utf-8'))
print(cli.recv(1024).decode())
