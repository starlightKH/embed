# 실습 4
import Jetson.GPIO as GPIO
import time

SERVO_PIN = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def set_angle(angle):
    duty = 2.5 + (angle / 180.0) * 10
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        set_angle(0)
        time.sleep(1)
        set_angle(90)
        time.sleep(1)
        set_angle(180)
        time.sleep(1)

except KeyboardInterrupt:
    print("종료")
    pwm.stop()
    GPIO.cleanup()