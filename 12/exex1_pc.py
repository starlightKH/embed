"""
추가 실습 1 - 외부 PC TCP 클라이언트

실행 위치:
    외부 PC

수정할 부분:
    SERVER_IP를 Jetson Orin Nano의 실제 IP 주소로 바꾼다.

실행:
    py extra1_pc_client.py
"""

import socket
import struct

# Jetson Orin Nano의 실제 IP 주소로 수정
SERVER_IP = "192.168.0.45"
SERVER_PORT = 12345


def receive_exact(sock, size):
    """지정한 크기만큼 데이터를 정확히 수신한다."""
    data = b""

    while len(data) < size:
        chunk = sock.recv(size - len(data))

        if not chunk:
            raise ConnectionError("Jetson 서버 연결이 종료되었습니다.")

        data += chunk

    return data


def receive_message(sock):
    """
    [4바이트 메시지 길이][UTF-8 메시지 본문] 형식으로 문자열을 받는다.
    """
    header = receive_exact(sock, 4)
    message_length = struct.unpack("!I", header)[0]

    body = receive_exact(sock, message_length)
    return body.decode("utf-8")


def send_message(sock, message):
    """
    문자열을 [4바이트 메시지 길이][UTF-8 메시지 본문] 형식으로 보낸다.
    """
    body = message.encode("utf-8")
    header = struct.pack("!I", len(body))

    sock.sendall(header + body)


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))

        print("=== PC TCP 클라이언트 실행 ===")
        print("Jetson 서버에 연결되었습니다.")
        print("종료하려면 /bye를 입력하세요.")

        while True:
            question = input("\n질문을 입력하세요: ").strip()

            if not question:
                print("질문을 입력해야 합니다.")
                continue

            send_message(client_socket, question)

            answer = receive_message(client_socket)

            print("\n=== SLM Response ===")
            print(answer)

            if question.lower() == "/bye":
                break

    except ConnectionRefusedError:
        print("연결이 거부되었습니다.")
        print("Jetson 서버가 먼저 실행되었는지 확인하세요.")

    except OSError as error:
        print("소켓 통신 오류:", error)

    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
