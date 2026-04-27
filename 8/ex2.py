#싱글 - 멀티 프로세스 - 멀티 스레딩 순으로 빠른 이유 기술

import time
import cv2
import threading
import multiprocessing

IMAGE_PATH = ["cat.jpg", "cow.jpg", "horse.jpg", "puppy.jpg"]
NUM_THREADS = 4
NUM_PROCESSES = 4


def load_image(path):
    # 이미지 파일 읽기
    img = cv2.imread(path)

    return img


def single_thread_test(image_paths):
    start_time = time.time()

    images = []

    # 한 번에 하나씩 순서대로 이미지 읽기
    for path in image_paths:
        img = load_image(path)
        images.append(img)

    end_time = time.time()

    print(f"싱글스레딩 실행 시간: {end_time - start_time:.4f}초")


def thread_worker(paths, result_list):
    # 스레드가 맡은 이미지들 읽기
    for path in paths:
        img = load_image(path)
        result_list.append(img)


def multi_thread_test(image_paths, num_threads):
    start_time = time.time()

    threads = []
    images = []

    chunk_size = len(image_paths) // num_threads

    for i in range(num_threads):
        start_idx = i * chunk_size

        if i == num_threads - 1:
            end_idx = len(image_paths)
        else:
            end_idx = (i + 1) * chunk_size

        paths = image_paths[start_idx:end_idx]

        # 스레드 생성
        t = threading.Thread(
            target=thread_worker,
            args=(paths, images)
        )

        threads.append(t)
        t.start()

    # 모든 스레드가 끝날 때까지 대기
    for t in threads:
        t.join()

    end_time = time.time()

    print(f"멀티스레딩 실행 시간: {end_time - start_time:.4f}초")


def process_worker(paths, result_queue):
    count = 0

    # 프로세스가 맡은 이미지들 읽기
    for path in paths:
        img = load_image(path)

        if img is not None:
            count += 1

    # 결과를 큐에 저장
    result_queue.put(count)


def multi_process_test(image_paths, num_processes):
    start_time = time.time()

    processes = []
    result_queue = multiprocessing.Queue()

    chunk_size = len(image_paths) // num_processes

    for i in range(num_processes):
        start_idx = i * chunk_size

        if i == num_processes - 1:
            end_idx = len(image_paths)
        else:
            end_idx = (i + 1) * chunk_size

        paths = image_paths[start_idx:end_idx]

        # 프로세스 생성
        p = multiprocessing.Process(
            target=process_worker,
            args=(paths, result_queue)
        )

        processes.append(p)
        p.start()

    # 모든 프로세스가 끝날 때까지 대기
    for p in processes:
        p.join()

    total_count = 0

    # 큐에서 결과 꺼내기
    while not result_queue.empty():
        total_count += result_queue.get()

    end_time = time.time()

    print(f"멀티프로세싱 실행 시간: {end_time - start_time:.4f}초")


if __name__ == "__main__":
    single_thread_test(IMAGE_PATH)

    time.sleep(2)

    multi_thread_test(IMAGE_PATH, NUM_THREADS)

    time.sleep(2)

    multi_process_test(IMAGE_PATH, NUM_PROCESSES)