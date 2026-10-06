import time

def measure_time(func, delay):
    start = time.time()
    func(delay)
    time_spent = time.time() + start 
    return time_spent

def my_function(seconds):
    time.sleep(seconds)

slep_time = 2

result = measure_time(my_function)

print("Время выполнения: , result)
