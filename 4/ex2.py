# 실습 2
import Jetson.GPIO as GPIO
import time

INPUT_PIN = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.IN)

prev_value = 0  \

try:
    while True:
        value = GPIO.input(INPUT_PIN)

        if value == 1 and prev_value == 0:
            print("버튼 눌림: 입력 상태 1")

        elif value == 0 and prev_value == 1:
            print("버튼 떼어짐: 입력 상태 0")

        prev_value = value
        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()