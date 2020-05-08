import time
from time import sleep

for i in range(10):
    millis = int(round(time.time() * 1000))
    sleep(0.00001)
    print(millis)
