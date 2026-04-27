# 실습 5
import spidev
import time
import Jetson.GPIO as GPIO
import time


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

PWM_PIN = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM_PIN, GPIO.OUT)

pwm = GPIO.PWM(PWM_PIN,1000)
pwm.start(0)

def analogRead(channel):
    buf = [(1<<2)|(1<<1)|((channel&0x04)>>2), (channel&0x03)<<6, 0]
    buf = spi.xfer(buf)
    adcValue = ((buf[1]&0x0F)<<8)|buf[2]
    return adcValue

try:
    while True:
        senvalue = analogRead(0) * (3.3/4095)
        print("%0.2f V" %senvalue)
        time.sleep(0.01)
        duty = (senvalue / 3.3) * 100
        pwm.ChangeDutyCycle(duty)

        
except KeyboardInterrupt:
    pass

spi.close
pwm.stop()
GPIO.cleanup()
