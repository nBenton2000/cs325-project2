

import socket
import sys
import ipaddress



PORT = 65432  # The port used by the server
HOST = "192.168.1.15"

DINGUS_SERVER = "192.168.122.200"
BINGUS_GUEST = "192.168.122.46"



def send():
    message = input("Enter Message (max 4096 characters): ")
    ip = ipCheck()
    
    addr = ((ip, PORT))
    print(f"Starting connection to {addr}")
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #socket1.setblocking(True)
    #socket1.connect(addr)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket1:
        socket1.settimeout(30.0)#Time out of 30 seconds if not received
        socket1.connect((ip, PORT))
        socket1.settimeout(None)#Always set timeout to none before sending.
        print("Sending")
        socket1.sendall(bytes(message, 'utf-8'))
        data = socket1.recv(1024)
        print("Message sent successfully.")
        socket1.recv(1024)
        print(data.decode(), end="\n")

def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("192.168.122.138", PORT)) #Inner brackets define a tuple CHANGE HOSTNAME TO THIS MACHINES NAME
        print("Waiting for message on port 65432")
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
                    print("Message:")
                    print(data.decode(),end="\n")
                    print("End of message")
                    conn.send(bytes('Found you', 'utf-8'))
                    exit = True

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
        menuOption()

def menuDisplay():
    print("===The Python Communicator===\n" +
     "1) Send Message\n" +
     "2) Receive Message\n" + 
     "0) Exit")

##Will handle getting the ip address formatted right
def ipCheck():
    keepgoing = True
    ip = ""
    while(keepgoing):
        ip = input("Enter Recipient IP:")
        try:
            ip_object = ipaddress.ip_address(ip)
            keepgoing = False
        except ValueError:
            print("Error not a valid IPv4 Address")

    return ip


if __name__ == '__main__':
    menuOption()