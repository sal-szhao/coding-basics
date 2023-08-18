import socket

ip_port = ('127.0.0.1', 8080)
BUFSIZE = 1024

def client_tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect_ex(ip_port)                

    while True:                            
        msg = input('>>: ').strip()
        if len(msg) == 0: continue
        s.send(msg.encode('utf-8'))       
        feedback = s.recv(BUFSIZE)        
        print(feedback.decode('utf-8'))

    s.close() 

def client_udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input('>>: ').strip()
        s.sendto(msg.encode('utf-8'), ip_port)
        res = s.recvfrom(1024)
        print(res)

if __name__ == "__main__":
    import sys

    if sys.argv[1] == "tcp":
        client_tcp()
    elif sys.argv[1] == "udp":
        client_udp()
