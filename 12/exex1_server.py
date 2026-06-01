"""
추가 실습 1 - Jetson Orin Nano TCP 서버

실행 위치:
    Jetson Orin Nano

기능:
    1. PC 클라이언트에서 질문을 TCP/IP 소켓으로 수신
    2. 받은 질문을 Jetson 내부의 Ollama HTTP API로 전달
    3. Ollama가 생성한 답변을 PC 클라이언트로 전송

실행:
    python3 extra1_jetson_server.py
"""

import socket
import struct
import requests

HOST = "0.0.0.0"       # 모든 네트워크 인터페이스에서 연결 허용
PORT = 12345            # PC 클라이언트와 맞춰야 하는 포트 번호

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "gemma3:1b"


def receive_exact(sock, size):
    """지정한 크기만큼 데이터를 정확히 수신한다."""
    data = b""

    while len(data) < size:
        chunk = sock.recv(size - len(data))

        if not chunk:
            raise ConnectionError("클라이언트 연결이 종료되었습니다.")

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


def ask_ollama(question):
    """받은 질문을 Ollama API에 전달하고 생성된 답변을 반환한다."""
    data = {
        "model": MODEL_NAME,
        "prompt": question,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=data, timeout=180)
    response.raise_for_status()

    result = response.json()
    return result["response"]


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 프로그램을 다시 실행할 때 포트 재사용이 가능하도록 설정
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("=== Jetson TCP 서버 실행 ===")
    print("PC 클라이언트의 연결을 기다리는 중입니다.")
    print("포트 번호:", PORT)

    try:
        while True:
            client_socket, client_address = server_socket.accept()

            print("\nPC 클라이언트가 연결되었습니다.")
            print("클라이언트 주소:", client_address)

            try:
                while True:
                    question = receive_message(client_socket)

                    print("\n=== PC에서 받은 질문 ===")
                    print(question)

                    # PC 클라이언트에서 /bye를 입력하면 연결 종료
                    if question.strip().lower() == "/bye":
                        send_message(client_socket, "연결을 종료합니다.")
                        print("클라이언트 연결을 종료합니다.")
                        break

                    try:
                        answer = ask_ollama(question)

                    except requests.RequestException as error:
                        answer = "Ollama API 통신 오류: " + str(error)

                    except (KeyError, ValueError) as error:
                        answer = "Ollama 응답 처리 오류: " + str(error)

                    print("\n=== Ollama가 생성한 답변 ===")
                    print(answer)

                    send_message(client_socket, answer)

            except ConnectionError:
                print("클라이언트 연결이 끊어졌습니다.")

            finally:
                client_socket.close()

    except KeyboardInterrupt:
        print("\n서버를 종료합니다.")

    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
