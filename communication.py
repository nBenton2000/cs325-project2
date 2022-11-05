

import socket
import sys

PORT = 65432  # The port used by the server
VM_IP = "192.168.1.15"
DINGUS_SERVER = '192.168.122.46'

def send():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(30.0)#Time out of 30 seconds if not received
        s.connect((ip, PORT))
        s.settimeout(None)#Always set timeout to none before sending.
        s.sendall(b"Hello, world")
        data = s.recv(1024)

        
def send():
    message = input("Enter Message (max 4096 characters): ")
    ip = input("Enter Recepient IP: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(30.0)#Time out of 30 seconds if not received
        s.connect((ip, PORT))
        s.settimeout(None)#Always set timeout to none before sending.
        s.sendall(message)
        data = s.recv(1024)



def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ALL_IP, PORT)) #Inner brackets define a tuple
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
    menuDisplay()
    option = input("Enter option: ")
    if option == "0":
        exit()
    elif option == "1":
        send()
    elif option == "2":
        receive()
    else:
        print("Error, invalid input")

def menuDisplay():
    print("===The Python Communicator===\n1) Send Message\n" +
     "2) Receive Message\n3) Exit")


if __name__ == '__main__':
    menuDisplay()
    menuOption()