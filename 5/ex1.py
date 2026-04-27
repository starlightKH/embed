import socket

HOST = '192.168.0.45'    # Jetson IP
PORT = 12345

# 소켓 생성
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 연결
client.connect((HOST, PORT))
txt = "Hello jetson"
txtover = txt * 256

# 데이터 송신
client.sendall(txt.encode())

# 데이터 수신
data = client.recv(1024).decode()
print("Received:", data)

# 종료
client.close()