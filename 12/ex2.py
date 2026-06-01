import requests

url = "http://127.0.0.1:11434/api/generate"

# 사용자에게 나라 이름 입력받기
city = input("알고 싶은 도시 이름을 입력하세요: ")

prompt = f"""
너는 도시 정보를 정리해주는 assistant야.

사용자가 질문한 도시:
- 도시 이름: {city}

아래 형식으로만 한국어로 출력해.

[도시 요약]
{city}가 어떤 도시인지 한 문장으로 설명해.

[랜드마크]
{city}의 랜드마크를 출력해.

[인구수]
{city}의 현재 인구수를 출력해.

[특산물]
{city}의 특산물을 출력해. 가능하면 2개정도.

[면적]
{city}의 면적을 출력해.

[주의]
정보가 최신이 아닐 수 있으면 그 점을 한 문장으로 설명해.
"""

data = {
    "model": "gemma3:1b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=data)
response.raise_for_status()

result = response.json()

print("\n=== 도시 정보 출력 ===")
print(result["response"])
