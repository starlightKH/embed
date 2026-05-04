# -v /dev:/dev의 의미 설명 및 왜 실행결과가 다른지 해석.

# mkdir ~/docker_workspace
# sudo docker run -it --rm --privileged \
# -p 8888:8888 \
# -v /dev:/dev \
# -v ~/docker_workspace:/workspace \
# --runtime=nvidia \
# my_torch:1.0 /bin/bash

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


# sudo docker run -it --rm --privileged \
# -p 8888:8888 \
# -v ~/docker_workspace:/workspace \
# --runtime=nvidia \
# my_torch:1.0 /bin/bash