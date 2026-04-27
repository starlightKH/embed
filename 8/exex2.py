import Jetson.GPIO as GPIO
import time
import multiprocessing

LED_PIN = 33   # PWM 가능한 핀으로 수정해서 사용


def input_process(speed_value):
    while True:
        try:
            value = int(input("속도 입력 0~10: "))

            if 0 <= value <= 10:
                speed_value.value = value
                print(f"속도 변경: {value}")

            else:
                print("0~10 사이 정수를 입력하세요.")

        except:
            print("정수를 입력하세요.")


def pwm_process(speed_value):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)

    pwm = GPIO.PWM(LED_PIN, 1000)   # 1000Hz PWM
    pwm.start(0)

    try:
        while True:
            speed = speed_value.value

            # 0이면 가장 느리게, 10이면 가장 빠르게
            delay = 0.1 - (speed * 0.009)

            if delay < 0.01:
                delay = 0.01

            # LED 밝아짐
            for duty in range(0, 101):
                pwm.ChangeDutyCycle(duty)
                time.sleep(delay)

            # LED 어두워짐
            for duty in range(100, -1, -1):
                pwm.ChangeDutyCycle(duty)
                time.sleep(delay)

    except KeyboardInterrupt:
        print("PWM 종료")

    finally:
        pwm.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    # 프로세스끼리 공유할 속도값
    speed_value = multiprocessing.Value("i", 5)

    p1 = multiprocessing.Process(target=input_process, args=(speed_value,))
    p2 = multiprocessing.Process(target=pwm_process, args=(speed_value,))

    p1.start()
    p2.start()

    try:
        p1.join()
        p2.join()

    except KeyboardInterrupt:
        print("프로그램 종료")

        p1.terminate()
        p2.terminate()

        p1.join()
        p2.join()