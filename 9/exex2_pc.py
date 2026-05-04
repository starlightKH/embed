import socket
import struct

HOST = '젯슨IP주소'
PORT = 9999

SAVE_PATH = 'received_image.jpg'

def recv_all(sock, size):
    data = b''

    while len(data) < size:
        packet = sock.recv(size - len(data))

        if not packet:
            return None

        data += packet

    return data

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

try:
    header = recv_all(client, 4)

    if header is None:
        print("헤더 수신 실패")
    else:
        image_size = struct.unpack('!I', header)[0]
        print("수신할 이미지 크기:", image_size, "bytes")

        image_data = recv_all(client, image_size)

        if image_data is None:
            print("이미지 데이터 수신 실패")
        else:
            with open(SAVE_PATH, 'wb') as f:
                f.write(image_data)

            print("이미지 저장 완료:", SAVE_PATH)

finally:
    client.close()