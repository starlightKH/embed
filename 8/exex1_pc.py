# 딜레이 없는거 체크 + 해상도 입력 스레드 추가

import socket
import struct
import cv2
import numpy as np
import threading

SERVER_IP = '192.168.0.45'
PORT = 9999

stop_event = threading.Event()


def recv_all(sock, size):
    data = b''

    while len(data) < size:
        packet = sock.recv(size - len(data))

        if not packet:
            return None

        data += packet

    return data


def input_resolution(client):
    while not stop_event.is_set():
        try:
            user_input = input('해상도 입력 예) 640 480 / 종료 q: ')

            if user_input == 'q':
                stop_event.set()
                break

            width, height = map(int, user_input.split())

            # 해상도 2개를 8바이트로 전송
            data = struct.pack('!II', width, height)
            client.sendall(data)

            print(f'해상도 전송: {width} x {height}')

        except:
            print('입력 오류. 예: 640 480')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

# input() 전용 스레드
input_thread = threading.Thread(
    target=input_resolution,
    args=(client,)
)

input_thread.start()

try:
    while not stop_event.is_set():
        header = recv_all(client, 4)

        if header is None:
            break

        data_len = struct.unpack('!I', header)[0]

        image_data = recv_all(client, data_len)

        if image_data is None:
            break

        np_data = np.frombuffer(image_data, dtype=np.uint8)
        frame = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

        if frame is None:
            continue

        cv2.imshow('Streaming', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()
            break

except KeyboardInterrupt:
    print('종료')

finally:
    stop_event.set()
    input_thread.join()

    client.close()
    cv2.destroyAllWindows()