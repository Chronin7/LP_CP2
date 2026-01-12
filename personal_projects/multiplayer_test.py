import utill_functions
import socket
import threading
print(utill_functions.get_ip_adress())
HOST = utill_functions.get_ip_adress()
PORT = 65432  
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            # Receive data (buffer size 1024 bytes)
            data = conn.recv(1024)
            if not data:
                break
            # Decode the message and print
            print(f"Client: {data.decode('utf-8')}")
        except ConnectionResetError:
            break
    conn.close()
    print(f"Connection with {addr} closed")
def send_mesage(conn, addr):
    conn.send(input("you:").encode('utf-8'))
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            # Accept an incoming connection
            conn, addr = s.accept()
            # Handle client in a new thread
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
            host_thread=threading.Thread(target=send_mesage,args=(conn, addr))
            host_thread.start()

if __name__ == "__main__":
    start_server()
