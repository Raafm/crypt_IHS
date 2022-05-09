import socket
from threading import Thread
from crypt_class import *

cry = Cryptographer(Key = 17)

cry.generate_lock(2**5)
    

def writeMSG(server, conexao):
    while True:
        msg = input() 
        
        if msg == 'bye': return
        
        msg = cry.encrypt(msg)
        conexao.sendto(msg.encode(), server)
    

def receiveMSG(server,conexao):
    while True:
        msg, endereco = conexao.recvfrom(1024)
        msg= msg.decode('utf8')

        if msg == 'bye':
            conexao.sendto("closing connections".encode(), server)
            conexao.close()
        else:
            try:
                print("try to decrypt: ",msg)
                msg = cry.decrypt(int(msg))
            except:
                1+1
            print(msg)

def key_exchange(conexao,server):
    # pedido de criptografia
    
    # enviando minha chave publica (cadeado)
    cadeado = (cry.my_lock,cry.my_N)
    print("cadeado =", cadeado)
    crypt_request = "crypt request: " + str(cadeado)
    conexao.sendto(crypt_request.encode(), server)

    # esperando receber chaves publicas do server
    cadeado = conexao.recvfrom(1024)[0].decode('utf8')
    print("servidor:", cadeado)
    cadeado = cadeado.split(": ")[1]
    print(cadeado)
    cadeado = eval(cadeado)
    print("cadeado:", cadeado,type(cadeado))
    cry.other_lock,cry.other_N = cadeado
    

def Client():
   #serverIP = input("Server IP: ")
   #Port = int(input("Port: "))
    
    serverIP,Port = '192.168.56.1',50000

    server = (serverIP, Port)

    conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conexao.connect((serverIP, Port))

    nick_name = str(input("Qual seu nickname: "))
    connection_request = "connection request " + nick_name 
    
    print("enviando pedido de conexao:",connection_request)
    conexao.sendto(connection_request.encode(), server)
    print("status:",conexao.recvfrom(1024)[0].decode('utf8'))
   
    key_exchange(conexao, server)

    escrever = Thread(target=writeMSG,args = (server,conexao))
    
    ouvir = Thread(target = receiveMSG,args = (server,conexao))

    ouvir.start()
    escrever.start()

    escrever.join()
    conexao.close()


if __name__ ==  '__main__':
    Client()