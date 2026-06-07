"""
추가 실습 2 - 출력 형식 선택에 따른 prompt 변경

실행 위치:
    외부 PC

수정할 부분:
    BOARD_IP를 Jetson Orin Nano의 실제 IP 주소로 바꾼다.

기능:
    1. 질문 주제를 입력받는다.
    2. 출력 형식을 선택받는다.
    3. 선택한 번호에 따라 서로 다른 구조의 prompt를 생성한다.
    4. Jetson의 Ollama API에 prompt를 보내고 응답을 출력한다.

실행:
    py extra2_prompt_selector.py
"""

import requests

# Jetson Orin Nano의 실제 IP 주소로 수정
BOARD_IP = "192.168.0.45"

URL = "http://" + BOARD_IP + ":11434/api/generate"
MODEL_NAME = "gemma3:1b"


def make_prompt(topic, number):
    """선택한 출력 형식에 맞는 prompt를 생성한다."""

    if number == "1":
        return f"""
다음 주제의 핵심 내용을 한국어 한 문장으로만 요약해.
부가 설명이나 목록은 작성하지 마.

주제: {topic}
""".strip()

    elif number == "2":
        return f"""
다음 주제를 초보자도 이해할 수 있도록 한국어로 설명해.
반드시 항목별로 구분하고, 각 항목은 글머리표를 사용해.

주제: {topic}

[핵심 개념]
[사용하는 이유]
[장점]
[주의할 점]
""".strip()

    elif number == "3":
        return f"""
다음 주제를 한국어 보고서 형식으로 작성해.
반드시 아래 목차를 사용해.

주제: {topic}

1. 개요
2. 필요성
3. 동작 원리 또는 활용 방법
4. 장점
5. 결론
""".strip()

    elif number == "4":
        return f"""
다음 주제와 관련하여 오류가 발생했다고 가정하고
한국어 오류 원인 분석 형식으로 답변해.
확실하지 않은 내용은 단정하지 말고 확인 방법도 함께 작성해.

주제: {topic}

[발생 가능한 증상]
[가능한 원인]
[확인 방법]
[해결 방법]
[추가 점검 사항]
""".strip()

    else:
        return None


def main():
    topic = input("주제를 입력하세요: ").strip()

    if not topic:
        print("주제를 입력해야 합니다.")
        return

    print("\n출력 형식을 선택하세요.")
    print("1. 한 문장 요약")
    print("2. 항목별 설명")
    print("3. 보고서 형식")
    print("4. 오류 원인 분석 형식")

    number = input("번호를 입력하세요: ").strip()

    prompt = make_prompt(topic, number)

    if prompt is None:
        print("1~4 중 하나의 번호를 입력해야 합니다.")
        return

    print("\n=== 생성된 Prompt ===")
    print(prompt)

    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(URL, json=data, timeout=180)
        response.raise_for_status()

        result = response.json()

        print("\n=== SLM Response ===")
        print(result["response"])

    except requests.ConnectionError:
        print("\nJetson 보드에 연결하지 못했습니다.")
        print("BOARD_IP와 Ollama 외부 접속 설정을 확인하세요.")

    except requests.Timeout:
        print("\n응답 시간이 초과되었습니다.")

    except requests.RequestException as error:
        print("\nAPI 통신 오류:", error)

    except (KeyError, ValueError) as error:
        print("\n응답 처리 오류:", error)


if __name__ == "__main__":
    main()
