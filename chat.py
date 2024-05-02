import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(5)

print("Chat server started on port 12345")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} established.")

    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == "exit":
            break
        print(f"Client: {message}")

        reply = input("You: ")
        client_socket.send(reply.encode())

    client_socket.close()
    print(f"Connection from {address} closed.")
