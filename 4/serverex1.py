# tcp_server_jetson.py
import socket
import struct
import Jetson.GPIO as GPIO
import time

LED_PIN = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)


HOST = '0.0.0.0'
PORT = 12345





def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:



    server.bind((HOST, PORT))
    server.listen(1)
    print("서버 대기 중...")

    conn, addr = server.accept()
    print("Connected by", addr)

    while True:

        data = recvall(conn, 4)

        if data is None:
            print("데이터 수신 실패")
            break

        recv_value = struct.unpack('!i', data)[0]
        print("받은 값:", recv_value)
        if recv_value == 1:
            GPIO.output(LED_PIN, GPIO.HIGH)

        elif recv_value == 0: 
            GPIO.output(LED_PIN, GPIO.LOW)



        if recv_value < 0:
            conn.sendall("Hello PC".encode('utf-8'))
            break
        
    conn.close()

finally:
    print("서버 종료")
    server.close()
    GPIO.cleanup()