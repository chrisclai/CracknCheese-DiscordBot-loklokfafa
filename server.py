import socket
import json
import sys
from _thread import *
import threading
import time

# Find info
def new_json():
    with open('accounts/accounts.json') as read_file:
            accounts = json.load(read_file)
            return accounts

if len(sys.argv) != 2:
    print("Usage: python3 server.py <hostID>")
    sys.exit(1)

HOST = sys.argv[1]
PORT = 8009
BUFFER_SIZE = 8162
SENSOR_COUNT = 1
TIME_OUT = 5

def read_async(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected to read_async thread.")
    while True:
        try:
            # Recieve data from client and print out
            data_recv = conn.recv(BUFFER_SIZE).decode('utf-8')
            print(f"Recieved: {data_recv}, checking for compatibility...")
        except Exception as e:
            # If the connection to the server has lost, print exception and exit
            print(type(e), e)
            break

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT)) # Bind System Socket
    s.listen(SENSOR_COUNT) # Listen for only 1 connection
    s.settimeout(TIME_OUT)  # How much time to wait for before stopping blocking function
    print(f"Listening on {HOST}:{str(PORT)}")
    conn = 0
    addr = 0
    # Continually check for connections
    while True:
        try:
            conn, addr = s.accept()
            print(f"Connection from {addr} has been established!")
            # Start thread to read information from client
            read_thread = threading.Thread(target = read_async, args = (conn, addr))
            read_thread.start()
        except KeyboardInterrupt: # In the case of ctrl+c, stop the code
            if conn:
                print(f"Closing Client Connection")
                conn.close()
            if s:
                print(f"Closing Server Connection")
                s.close()
            print("Terminating.")
            sys.exit(1)
        except:
            pass

if __name__ == '__main__':
    main()