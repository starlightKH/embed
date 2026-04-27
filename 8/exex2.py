import Jetson.GPIO as GPIO
import time
import multiprocessing

LED_PIN = 33   # PWM 가능한 핀으로 수정


def pwm_process(speed_value, stop_event):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)

    pwm = GPIO.PWM(LED_PIN, 1000)
    pwm.start(0)

    try:
        while not stop_event.is_set():
            speed = speed_value.value

            # 0이면 느리게, 10이면 빠르게
            delay = 0.1 - (speed * 0.009)

            if delay < 0.01:
                delay = 0.01

            # 밝아짐
            for duty in range(0, 101):
                if stop_event.is_set():
                    break

                pwm.ChangeDutyCycle(duty)
                time.sleep(delay)

            # 어두워짐
            for duty in range(100, -1, -1):
                if stop_event.is_set():
                    break

                pwm.ChangeDutyCycle(duty)
                time.sleep(delay)

    finally:
        pwm.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    # 프로세스끼리 공유할 속도 값
    speed_value = multiprocessing.Value("i", 5)

    # 종료 신호
    stop_event = multiprocessing.Event()

    # PWM 제어 프로세스 생성
    p = multiprocessing.Process(
        target=pwm_process,
        args=(speed_value, stop_event)
    )

    p.start()

    try:
        while True:
            user_input = input("속도 입력 0~10 / 종료 q: ")

            if user_input == "q":
                stop_event.set()
                break

            try:
                value = int(user_input)

                if 0 <= value <= 10:
                    speed_value.value = value
                    print(f"속도 변경: {value}")

                else:
                    print("0~10 사이 정수를 입력하세요.")

            except ValueError:
                print("정수를 입력하세요.")

    except KeyboardInterrupt:
        print("종료")

    finally:
        stop_event.set()
        p.join()