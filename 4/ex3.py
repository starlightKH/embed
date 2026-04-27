# 실습 3
import Jetson.GPIO as GPIO
import time

PWM_PIN = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM_PIN, GPIO.OUT)

pwm = GPIO.PWM(PWM_PIN, 1000)
pwm.start(0)

try:
    while True:
        for dc in range(0, 101):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()