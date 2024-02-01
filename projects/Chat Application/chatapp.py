import socket
import threading

# Server configuration
HOST = "127.0.0.1"
PORT = 12345

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []


def handle_client(client_socket, addr):
    with client_socket:
        print(f"New connection from {addr}")
        clients.append(client_socket)
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            for client in clients:
                if client != client_socket:
                    client.send(data)


def main():
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, addr)
        )
        client_handler.start()


if __name__ == "__main__":
    main()


import socket
import threading

# Client configuration
HOST = "127.0.0.1"
PORT = 12345


def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        print(data)


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode())


if __name__ == "__main__":
    main()
