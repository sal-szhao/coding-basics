import socket, struct, json
import subprocess

phone=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)

while True:
    conn, addr = phone.accept()
    while True:
        cmd = conn.recv(1024)
        if not cmd: break
        print('cmd: %s' % cmd)

        res = subprocess.Popen(cmd.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        err = res.stderr.read()
        print(err)
        if err:
            back_msg = err
        else:
            back_msg = res.stdout.read()

        conn.send(struct.pack('i', len(back_msg))) # Send the length of back_msg first.
        conn.sendall(back_msg) # Send the actual data, ensures all the data has been sent.

    conn.close()