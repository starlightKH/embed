import requests

url = "http://127.0.0.1:11434/api/generate"

# 사용자에게 prompt 입력받기
user_prompt = input("질문을 입력하세요: ")

data = {
    "model": "gemma3:1b",
    "prompt": user_prompt,
    "stream": False
}

response = requests.post(url, json=data)
response.raise_for_status()

result = response.json()

print("=== LLM Response ===")
print(result["response"])
