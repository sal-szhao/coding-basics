import socket, time, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(('127.0.0.1',8080))

while True:
    # Send message.
    msg = input('>>: ').strip()
    if len(msg) == 0: continue
    if msg == 'quit': break
    s.send(msg.encode('utf-8'))

    # Receive message.
    l = s.recv(4)                   # Get the packed length of the header, default length to be 4.
    x = struct.unpack('i', l)[0]     # Unpack the data to get the actual length.
    print(type(x), x)
    r_s = 0
    data = b''
    while r_s < x:
        r_d = s.recv(1024)
        data += r_d
        r_s += len(r_d)

    print(data.decode('utf-8'))
    # print(data.decode('gbk')) # windows default encoding is gbk.
