import sys

def main():

    if len(sys.argv) != 4:
        print("[오류] 전달한 인자의 개수가 올바르지 않습니다.")
        sys.exit(1)

    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("[오류] 0으로 나눌 수 없습니다.")
            sys.exit(1)
        result = num1 / num2
    else:
        print(f"[오류] 지원하지 않는 연산자입니다: {operator}")
        sys.exit(1)

    print("=== 계산 결과 ===")
    print(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])
    print(f"첫 번째 숫자 : {num1}")
    print(f"연산자      : {operator}")
    print(f"두 번째 숫자 : {num2}")
    print(f"결과        : {result}")

if __name__ == "__main__":
    main()