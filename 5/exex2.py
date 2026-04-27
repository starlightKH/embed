# pc_client.py
import socket
import struct
import time

HOST = '192.168.0.45'    # Jetson IP
PORT = 12345

# 소켓 생성
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 연결
client.connect((HOST, PORT))

def send_data(value):
    data = struct.pack('!i', value)   # 정수 value를 4바이트로 변환
    client.sendall(data)              # 서버로 전송


try:
    while True:
        for dc in range(0, 101):
            time.sleep(0.01)
            send_data(dc)
        for dc in range(100, -1, -1):
            time.sleep(0.01)
            send_data(dc)
except KeyboardInterrupt:
    print("종료")

finally:
    client.close()

