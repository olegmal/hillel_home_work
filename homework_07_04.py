# 1.Напишіть декоратор, який визначає час виконання функції.
# Заміряйте час виконання функцій з попереднього ДЗ

import time

def execution_time(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        print((time.perf_counter() - start_time))

        return result
    return wrapper


@ execution_time
def add(x, y):
    time.sleep(1)
    return x + y

result = add(4, 8)
print(result)




