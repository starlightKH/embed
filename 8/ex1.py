import time
import math

RUN_SECONDS = 60   # 60초 동안 실행


def heavy_work():
    start_time = time.time()
    count = 0
    result = 0.0

    # 60초 동안 CPU 연산 반복
    while time.time() - start_time < RUN_SECONDS:
        for i in range(1, 100000):
            result += math.sqrt(i) * math.sin(i)

        count += 1

        if count % 100 == 0:
            elapsed = time.time() - start_time

    print(f"result={result}")


heavy_work()