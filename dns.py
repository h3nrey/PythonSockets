import socket
from constants import *
import pickle

class DNS_server():
    def __init__(self):
        self.dns_address = (DNS_IP, DNS_PORT)
        self.ips_table = {
            # 'udpserver': (UDP_IP, UDP_PORT),
            # 'tcpserver': (TCP_IP, TCP_PORT)        
        }
        self.dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dns_socket.bind(self.dns_address)
        print(f"Servidor dns rodando em {DNS_IP} na porta {DNS_PORT}")
        
        self.handle_conection()
        
    def handle_conection(self):
        while True:
            request, client_address = self.dns_socket.recvfrom(BUFFER_SIZE)
            
            # format GET/REGISTER-value
            request = request.decode("utf-8").split("-")
            method = request[0]
            data = request[1]
            
            # GET format = "REGISTER-udpserver"
            if(method == "GET"):
                response = self.get_ip_from_domain(data).encode("utf-8")
                self.dns_socket.sendto(response, client_address)
                
            # Regiter format = "REGISTER-udpserver,IP/PORT"
            elif(method == "REGISTER"):
                value = data.split(",")
                response = self.register_ips(value).encode("utf-8")
                self.dns_socket.sendto(response, client_address)
    
    def close(self):
        self.ips_table = {}
        self.dns_socket.close()            
                
    def get_ip_from_domain(self, domain) :
        ip = self.ips_table[domain]
        ip = f"{ip[0]},{ip[1]}"
        return ip

    # value = (domain, address)
    def register_ips(self, value):
        print(value)
        domain, address = value
        
        print(f"value: {value[1]}")
        if(value[1] == 'NONE'):
            del self.ips_table[domain]
            print(self.ips_table)
            return "Registro removido com sucesso"
        
        self.ips_table[domain] = address.split("/")
        print(self.ips_table)
        return "Registro adicionado com sucesso"

DNS_server()
