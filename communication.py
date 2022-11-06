

import socket
import sys

PORT = 65432  # The port used by the server
HOST = "192.168.1.15"

DINGUS_SERVER = "192.168.122.200"
BINGUS_GUEST = "192.168.122.46"


def send():
    message = input("Enter Message (max 4096 characters): ")
    ip = input("Enter Recepient IP: ")

    addr = (HOST, PORT)
    print(f"Startomg connection to {addr}")
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.setblocking(False)
    socket1.connect(addr)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket1:
        socket1.settimeout(30.0)#Time out of 30 seconds if not received
        socket1.connect((ip, PORT))
        socket1.settimeout(None)#Always set timeout to none before sending.
        socket1.sendall(message)
        data = socket1.recv(1024)

def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((socket.gethostbyname("Host Name"), PORT)) #Inner brackets define a tuple CHANGE HOSTNAME TO THIS MACHINES NAME
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            exit = False
            while not exit:
                data = conn.recv(1024)
                if not data:
                    exit = True
                else:
                    print(data.decode(),end="#")
                conn.sendall(data)

def exit():
    print("Goodbye!")
    sys.exit()

def menuOption():
    option = input("Enter option: ")
    if option == "0":
        exit()
    elif option == "1":
        send()
    elif option == "2":
        receive()
    else:
        print("Error, invalid input")
        menuOption()

def menuDisplay():
    print("===The Python Communicator===\n" +
     "1) Send Message\n" +
     "2) Receive Message\n" + 
     "0) Exit")

if __name__ == '__main__':
    menuDisplay()
    menuOption()