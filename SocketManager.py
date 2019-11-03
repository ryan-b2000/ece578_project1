#! /usr/bin/env python3
import socket
import sys

SERVER_IP = '192.168.50.208'  # Standard loopback interface address (localhost)
SERVER_PORT = 65432        # Port to listen on (non-privileged ports are > 1023)



def SocketServer():
    print("Socket server function")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    except socket.error:
        print("Error opening socket!")
        return

    try:
        sock.bind((SERVER_IP, SERVER_PORT))
    
    except socket.error:
        print("Error binding socket!")
        return

    print("Listening on: " + SERVER_IP + ":" + str(SERVER_PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received data: " + str(data))
            conn.sendall(data)



def SocketClient():
    print("Socket client function")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Connecting to: " + SERVER_IP + ":" + str(SERVER_PORT))
        s.connect((SERVER_IP, SERVER_PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))


def Main(argv):
    if (argv[0] == 'Server'):
        SocketServer()
    else:
        SocketClient()

# ================================================================ #
if __name__ == "__main__":  
    Main(sys.argv[1:])