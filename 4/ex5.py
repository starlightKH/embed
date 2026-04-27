# 실습 5
import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

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
except KeyboardInterrupt:
    pass

spi.close