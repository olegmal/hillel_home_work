import threading
import time

my_list = []
def number_count(n):
    for i in range(1, n+1):
        my_list.append(i)
        time.sleep(1)

def number_count2(n):
    for i in range(1, n + 1):
        my_list.append(i)
        time.sleep(1)

first = threading.Thread(target=number_count, args=(4,))
first.start()

second = threading.Thread(target=number_count, args=(4,))
second.start()

first.join()
second.join()

print(my_list)



