import random
import signal
import resource
import os

CPU_TIME_LIMIT = 2 

if os.getenv("RUNNING_IN_DOCKER"):
    resource.setrlimit(resource.RLIMIT_CPU, (CPU_TIME_LIMIT, CPU_TIME_LIMIT))

def timeout_handler(signum, frame):
    raise TimeoutError("Ліміт часу CPU вичерпано!")

signal.signal(signal.SIGXCPU, timeout_handler)

try:
    print("Запуск лотереї...")

    while True:
        for _ in range(1000000):  
            seven = random.sample(range(1, 50), 7)
            six = random.sample(range(1, 37), 6)

except TimeoutError as e:
    print(e)

finally:
    print("Завершення роботи...")
