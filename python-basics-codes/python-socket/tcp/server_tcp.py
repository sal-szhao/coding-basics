import socket 

# Socket settings.
ip_port = ("127.0.0.1", 8080)
BUFSIZE = 1024 

# Create a socket.
# socket.SOCK_STREAM indicates that the socket uses TCP protocol.
# socket.AF_INET indicates that the socket supports IPv4 addresses.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ip_port)

# Determine the size of the half-open connection pool.
s.listen(5)

while True:
    print("Waiting for messages...")
    conn, addr = s.accept()         # Wait for a connection request.
    print(conn)
    print(addr)

    while True:
        msg = conn.recv(BUFSIZE)    # Recieve messages from the established connection.
        if len(msg) == 0: break
        print(msg, type(msg))
        conn.send(msg.upper())      # Send messages to the established connection.

    conn.close()

s.close()