# pc_client.py
import socket
import struct

HOST = '192.168.0.45'    # Jetson IP
PORT = 12345

Float_data = 45.7
data = struct.pack('!iif', 1, 2, Float_data)

# 소켓 생성
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 연결
client.connect((HOST, PORT))

# 데이터 송신
client.sendall(data)

# 데이터 수신
data = client.recv(1024).decode()
print("Received:", data)

# 종료
client.close()