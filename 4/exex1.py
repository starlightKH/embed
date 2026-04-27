import Jetson.GPIO as GPIO
import time

LED_PIN = 31
INPUT_PIN = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

prev_value = GPIO.input(INPUT_PIN)

try:
    while True:
        value = GPIO.input(INPUT_PIN)

        if value == 1 and prev_value == 0:
            print("버튼 눌림: 입력 상태 1")
            GPIO.output(LED_PIN, GPIO.HIGH)

        elif value == 0 and prev_value == 1:
            print("버튼 떼어짐: 입력 상태 0")
            GPIO.output(LED_PIN, GPIO.LOW)

        prev_value = value
        time.sleep(0.05)

except KeyboardInterrupt:
    print("종료")

finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()