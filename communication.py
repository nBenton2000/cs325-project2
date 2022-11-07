##Communication.py
#@Authors Nicolas Benton and Evan Escobedo
#Allows for the communication between two computers accross a
#network. 

import socket
import sys
import ipaddress


######################################################################
#EDIT HERE FOR YOUR SERVER
PORT = 65432  # The port used by the server
SERVER_IP = "192.168.122.138" # The ip address used by the server
######################################################################

#This function handles everything for the user performing the client side
#operations.  The user will specifiy an ip address to communicate with
#and a message to send to the server

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
        print(data.decode(), end="\n") #print a message recieved back from the server

#This function handles the server side tasks.  The method will wait for any input on 
# desired port.  Right now the bound ip address is hard coded in the config above with
# ip of the host and port desired to be used specified by the user
def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SERVER_IP, PORT)) #Inner brackets define a tuple CHANGE HOSTNAME TO THIS MACHINES NAME
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
                    conn.send(bytes('Hello Host Operating System', 'utf-8'))
                    conn.send(bytes('#<<END>>#', 'utf-8'))
                    exit = True
                    conn.close()

#Closes the program with a nice message
def exit():
    print("Goodbye!")
    sys.exit()


#Handles the menu for user input. 
def menuOption():
    menuDisplay()
    option = input("Enter option: ")
    if option == "0": #Quit option 
        exit()
    elif option == "1": #Client Side Option
        send()
    elif option == "2": #Server Side Option
        receive()
    else: #Invalid input
        print("Error, invalid input")
        menuOption() #Recursive call to loop

#Prints a string containing reference numbers for various user functions
def menuDisplay():
    print("===The Python Communicator===\n" +
     "1) Send Message\n" +
     "2) Receive Message\n" + 
     "0) Exit")

##Will handle getting the ip address formatted right.  Will continually prompt
#the user should the ip address be malformed.
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

#Call to start the program
if __name__ == '__main__':
    menuOption()