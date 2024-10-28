import socket

# Opprett ein socket-objekt
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koble til serveren
client_socket.connect(('localhost', 12345))

# Mottar meldinga frå serveren
data = client_socket.recv(1024)
print(f"Melding frå serveren: {data.decode()}")

# Send ei melding til serveren
client_socket.send(b"Takk, serveren!")

# Lukk tilkoplinga
client_socket.close()