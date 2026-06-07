import requests

url = "http://192.168.0.45:11434/api/generate"

data = {
    "model": "gemma3:1b",
    "prompt": "API에 대해서 설명해 줘",
    "stream": False
}

response = requests.post(url, json=data)

print("status code:", response.status_code)
print("response text:")
print(response.text)

# 일단 이 줄은 잠깐 주석 처리
# response.raise_for_status()

if response.status_code == 200:
    result = response.json()
    print("=== LLM Response ===")
    print(result["response"])
