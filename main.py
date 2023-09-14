from udp_client import UDP_client
from tcp_client import TCP_client
from tcp_server import TCP_server
from udp_server import UDP_server

from constants import FILLED_INPUT
from writetime import erase

if __name__ == "__main__":
    udp_c = UDP_client()
    tcp_c = TCP_client()
    
    erase()
    for input_value in FILLED_INPUT:
        print("UDP CLIENT")
        udp_c.run(input_value)
        print("TCP CLIENT")        
        tcp_c.run(input_value)