import socketserver

'''
SocketServer allows server to deal with concurrent requests at the same time.
1. Take a connection from the connection pool.
2. Start a thread(process) to handle the connection and data.
'''
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)
        # self.request == conn if it is a TCP protocol.
        while True:
            try:
                msg = self.request.recv(1024)
                if len(msg) == 0: break
                self.request.send(msg.upper())
            except Exception:
                break
        self.request.close()

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        client_data = self.request[0]
        server = self.request[1]
        client_addr = self.client_address
        print(f"data sent by client {client_addr} is {client_data}")
        server.sendto(client_data.upper(), client_addr) 

if __name__ == "__main__":
    import sys

    if sys.argv[1] == "tcp":
        s = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyTCPHandler)
        s.serve_forever()
    elif sys.argv[1] == "udp":
        s = socketserver.ThreadingUDPServer(('127.0.0.1', 8080), MyUDPHandler)
        s.serve_forever()