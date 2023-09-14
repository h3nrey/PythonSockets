import socket
import time
import pickle
from constants import *
from writetime import write_time

class TCP_client():
    def run(self, input_value):

        # socket TCP 
        self.client_socket = socket.socket(
            socket.AF_INET, 
            socket.SOCK_STREAM
        )
        
        # Getting ip from DNS 
        udp_socket = socket.socket(
            socket.AF_INET, 
            socket.SOCK_DGRAM
        )
        request = "GET-tcpserver".encode("utf-8")
        udp_socket.sendto(request, (DNS_IP, DNS_PORT))
        
        self.dns_reponse, _ = udp_socket.recvfrom(BUFFER_SIZE)
        self.server_address = (self.dns_reponse.decode("utf-8").split(",")[0], int(self.dns_reponse.decode("utf-8").split(",")[1]))
        print(self.server_address)
        
        
        self.client_socket.connect(self.server_address)
        self.send_requisition(input_value)
        self.get_response()
        self.calc_totaltime()
        print("\n")
        self.client_socket.close()
    
    def calc_totaltime(self):
        total_time = self.res_time - self.req_time
        write_time(total_time, "TCP")
        
    
    def send_requisition(self, input_value):
        # Pega os dados do usuário 
        poke_choosed = input_value
        msg = poke_choosed.encode("utf-8")
        
        # Envia os dados 
        self.client_socket.send(msg)
        
        # Captura tempo atual
        curr_time = time.time() * 1000
        self.req_time = curr_time
        
    
    def get_response(self):
        response = self.client_socket.recv(BUFFER_SIZE)
        response = pickle.loads(response)
        
        if(len(response) > 0):
            print(f"Pokemons")
            for pokemon in response:
                print(pokemon)
        else:
            print("Não há registro de pokemons com esse tipo")
        self.res_time = time.time() * 1000