import socket

ip_port = ('127.0.0.1', 9000)
BUFSIZE = 1024

udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_client.bind(ip_port)

while True:
    msg, addr = udp_server_client.recvfrom(BUFSIZE)
    print(msg, addr)
    udp_server_client.sendto(msg.upper(), addr)