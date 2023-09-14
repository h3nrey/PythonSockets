import socket
import pickle
from constants import *
from database import pokemons

class TCP_server:
    def __init__(self):    
        server_address = (TCP_IP, TCP_PORT) 
        self.connections = 0
        
        # TCP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(server_address)
        self.server_socket.listen(5)
        print(f"Servidor TCP ligado em {server_address}")
        
        # Register IP
        # UDP socket
        self.udpserver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        resquest = f"REGISTER-tcpserver,{TCP_IP}/{TCP_PORT}".encode("utf-8")
        self.udpserver_socket.sendto(resquest, (DNS_IP, DNS_PORT))
        dns_reponse, _ = self.udpserver_socket.recvfrom(BUFFER_SIZE)
        print(dns_reponse.decode("utf-8"))
        
        self.update()
        
    def close(self):
        resquest = f"REGISTER-tcpserver,NONE".encode("utf-8")
        self.udpserver_socket.sendto(resquest, (DNS_IP, DNS_PORT))
        dns_reponse, _ = self.udpserver_socket.recvfrom(BUFFER_SIZE)
        print(dns_reponse.decode("utf-8"))
        self.server_socket.close()
    
    def update(self):
        while True:
            if(self.connections >= 5):
                break;
            self.connections += 1
            # Pega requisição do cliente
            client_socket, address = self.server_socket.accept()
            data = client_socket.recv(BUFFER_SIZE)
            data = data.decode("utf-8")
            print(f"Buscando pokemons do tipo {data}...")

            # Envia a resposta para o cliente
            response = self.choose_pokemon(data)
            client_socket.send(response)
        self.close()

    def choose_pokemon(self, type_name):
        if type_name not in pokemons: 
            return pickle.dumps([])
        
        pokes = pokemons[type_name]
        return pickle.dumps(pokes)
    
if __name__ == "__main__":
    TCP_server()