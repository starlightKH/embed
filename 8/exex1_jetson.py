import socket
import struct
import cv2
import threading

HOST = '0.0.0.0'
PORT = 9999

width = 640
height = 480

resolution_lock = threading.Lock()
stop_event = threading.Event()


def recv_all(sock, size):
    data = b''

    while len(data) < size:
        packet = sock.recv(size - len(data))

        if not packet:
            return None

        data += packet

    return data


def receive_resolution(conn):
    global width, height

    while not stop_event.is_set():
        try:
            data = recv_all(conn, 8)

            if data is None:
                stop_event.set()
                break

            w, h = struct.unpack('!II', data)

            with resolution_lock:
                width = w
                height = h

            print(f'전송 해상도 변경: {width} x {height}')

        except:
            stop_event.set()
            break


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print('클라이언트 접속 대기 중...')
conn, addr = server.accept()
print('Connected by', addr)

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# 카메라 자체 해상도는 고정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

resolution_thread = threading.Thread(
    target=receive_resolution,
    args=(conn,)
)

resolution_thread.start()

try:
    while not stop_event.is_set():
        ret, frame = cap.read()

        if not ret:
            print('프레임 읽기 실패')
            break

        # 현재 입력된 해상도 가져오기
        with resolution_lock:
            w = width
            h = height

        # 카메라 설정을 바꾸지 않고 이미지 크기만 변경
        frame = cv2.resize(frame, (w, h))

        ok, encoded = cv2.imencode(
            '.jpg',
            frame,
            [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        )

        if not ok:
            print('인코딩 실패')
            break

        data = encoded.tobytes()
        header = struct.pack('!I', len(data))

        conn.sendall(header)
        conn.sendall(data)

except KeyboardInterrupt:
    print('종료')

finally:
    stop_event.set()
    resolution_thread.join()

    cap.release()
    conn.close()
    server.close()