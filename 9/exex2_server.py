# sudo docker run -it --rm --privileged \
# -p 8888:8888 \
# -p 9999:9999 \
# -v /dev:/dev \
# -v ~/docker_workspace:/workspace \
# --runtime=nvidia \
# my_torch:1.0 /bin/bash

import socket
import struct
import os

HOST = '0.0.0.0'
PORT = 9999

IMAGE_PATH = 'test.jpg'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(1)

print("이미지 전송 서버 대기 중...")

conn, addr = server.accept()
print("PC 연결됨:", addr)

try:
    if not os.path.exists(IMAGE_PATH):
        print("이미지 파일이 없습니다:", IMAGE_PATH)
    else:
        with open(IMAGE_PATH, 'rb') as f:
            image_data = f.read()

        data_size = len(image_data)

        header = struct.pack('!I', data_size)
        conn.sendall(header)
        conn.sendall(image_data)

        print("이미지 전송 완료")
        print("전송 크기:", data_size, "bytes")

finally:
    conn.close()
    server.close()