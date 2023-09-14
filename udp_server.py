import socket
import pickle
from constants import *
from database import pokemons

class UDP_server:
    def __init__(self):    
        server_address = (UDP_IP, UDP_PORT) 
        self.connections = 0
        
        # UDP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(server_address)
        
        # Register IP 
        resquest = f"REGISTER-udpserver,{UDP_IP}/{UDP_PORT}".encode("utf-8")
        self.server_socket.sendto(resquest, (DNS_IP, DNS_PORT))
        # register_ips(("udpserver", server_address))
        dns_reponse, _ = self.server_socket.recvfrom(BUFFER_SIZE)
        print(dns_reponse.decode("utf-8"))
        
        print(f"Servidor UDP ligado em {server_address}")
        
        self.update()
        
    def close(self):
        # Limpando do servidor dns 
        resquest = f"REGISTER-udpserver,NONE".encode("utf-8")
        self.server_socket.sendto(resquest, (DNS_IP, DNS_PORT))
        dns_reponse, _ = self.server_socket.recvfrom(BUFFER_SIZE)
        print(dns_reponse.decode("utf-8"))
        
        # Fechando servidor 
        self.server_socket.close()
    
    def update(self):
        while True:
            if(self.connections >= 5):
                break;
            self.connections += 1
            # Pega requisição do cliente
            data, client_address = self.server_socket.recvfrom(BUFFER_SIZE)
            
            data = data.decode("utf-8")
            print(f"Buscando pokemons do tipo {data}...")

            # Envia a resposta para o cliente
            response = self.choose_pokemon(data)
            self.server_socket.sendto(response, client_address)
        self.close()

    def choose_pokemon(self, type_name):
        if type_name not in pokemons: 
            return pickle.dumps([])
        
        pokes = pokemons[type_name]
        return pickle.dumps(pokes)

if __name__ == "__main__":
    UDP_server()