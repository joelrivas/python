import time
import datetime

lst = []

for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)

for i in lst:
    print(i)
