# 실습 1
import Jetson.GPIO as GPIO
import time

LED_PIN = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:  #d
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)

        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)

except KeyboardInterrupt:
    print("종료합니다.")
finally:
    GPIO.cleanup()