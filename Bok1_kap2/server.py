import socket

# Opprett ein socket-objekt (TCP(SOCK_STREAM) med IPv4(AF_INET))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socketen til ei adresse og ein port
server_socket.bind(('localhost', 12345))

# Lytta etter tilkoplingar (maks 5 køplassar)
server_socket.listen(5)

print("Serveren ventar på tilkopling...")

# Aksepter ei tilkopling
client_socket, client_address = server_socket.accept()
print(f"Tilkopla til {client_address}")

# Send ei melding til klienten
client_socket.send("Hei frå serveren!".encode())

# Mottar data frå klienten (opsjonelt)
data = client_socket.recv(1024)
print(f"Melding frå klienten: {data.decode()}")

# Lukk tilkoplinga
client_socket.close()
server_socket.close()

'''
UDP
'''
import socket

# Opprettar ein UDP-socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind sokkelen til ei adresse og ein port
server_socket.bind(("127.0.0.1", 12345))

print("UDP-serveren er klar til å ta imot data...")

while True:
    # Motta data frå klienten
    data, addr = server_socket.recvfrom(1024)  # 1024 byte buffer
    print(f"Motta melding frå {addr}: {data.decode()}")
    server_socket.sendto('Hei'.encode(),addr)
    
