### Multithreading with Thread Pool Executor
from concurrent.futures import ThreadPoolExecutor
import time


def print_numbers(number):
    time.sleep(.5)
    return f"Number: {number}"

numbers = [1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers,numbers)
    
for result in results:
    print(result)


## This is how we use Thread pool executor for multi threading 