import socket
from threading import Thread
from crypt_class import *

print("\t\t\t====>  UDP CHAT APP  <=====")
print("==============================================")
ip, port = "",50000 #"192.168.56.1",50000
server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
server.bind((ip, port))

hostname = socket.getfqdn()
print('hostname:',hostname)
print("IP Address:",socket.gethostbyname_ex(hostname))

clients     = []
client_name = {}
client_lock = {}
cry = Cryptographer(Key = 29)
cry.generate_lock()

def accept_crypt(mensagem,ClientAdress):
    str_lock = mensagem.decode().split(': ')[1]
    print("accept_crypt mensagem: ",mensagem)
    print(str_lock, type(str_lock))
    lock = eval(str_lock)
    print(lock, type(lock))
    client_lock[ClientAdress] = lock

    cadeado_server = "meu cadeado: " +  str((cry.my_lock, cry.my_N)) 
    server.sendto(cadeado_server.encode(),ClientAdress)


def accept_client(ClientName,ClientAdress):

    ClientName = str(ClientName).split(' ')[2][:-1]
    clients.append(ClientAdress)
    client_name[ClientAdress] = ClientName
    print("client:", ClientName,"connected")
    server.sendto("voce esta conectado".encode(),ClientAdress)



#envia mensagem para todo mundo
def Broadcast(msg,author):
    msg = '\n' + client_name[author] + "\n>>"+ msg 
    print(msg)
    for ClientAdress in clients:
        if ClientAdress == author: continue
        server.sendto((msg).encode(),ClientAdress)

on = True
def Server():
    global on
    while on:
        mensagem,ClientAdress = server.recvfrom(1024)
        
        if "connection request" in mensagem.decode():
            accept_client(mensagem,ClientAdress)

        if "crypt request: " in mensagem.decode():
            accept_crypt(mensagem,ClientAdress)

        else:
            mensagem = mensagem.decode()
            
            try:
                print("try to decrypt: ",mensagem)
                mensagem = cry.decrypt(int(mensagem))
            except:
                1+1
            Broadcast(mensagem,ClientAdress)


    
def writeMSG():
    global on
    while True:
        msg = input() 
        
        if msg == 'bye': on = False;return
        
        for ClientAdress in clients:
            try:
                Lock,N = client_lock[ClientAdress]
                msg = cry.encrypt(msg,Lock,N)
            except:
                1+1
            server.sendto((msg).encode(),ClientAdress) 

if __name__ == "__main__":
    escrever = Thread(target=writeMSG)
    escrever.start()
    Server()
    escrever.join()
    server.close()
    
