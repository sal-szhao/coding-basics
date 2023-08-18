import socket

ip_port = ('127.0.0.1', 8080)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect_ex(ip_port)                    # Try to establish the connection.

while True:                            
    msg = input('>>: ').strip()
    if len(msg) == 0: continue
    s.send(msg.encode('utf-8'))         # Send messages through the connection.
    feedback = s.recv(BUFSIZE)            # Receive messages from the connection. 
    print(feedback.decode('utf-8'))

s.close() 