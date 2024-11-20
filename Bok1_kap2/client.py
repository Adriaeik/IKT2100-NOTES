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

'''
UDP
'''
import socket

# Opprettar ein UDP-socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Adressa og porten til serveren
server_address = ("127.0.0.1", 12345)

# Send ein melding til serveren
melding = "Hei frå UDP-klienten!"
client_socket.sendto(melding.encode(), server_address)

print("Melding sendt til serveren!")
while(1):
    data = client_socket.recvfrom(1024)
    print(data)