'''
Real-World Example: Multiprocessing for Cpu-bound Tasks
Scenario: Factorial Calculation
Factorial Calculations, especially for large numbers involves significant 
computational work. Multiprocessing can be used to distribute the workload across
multiple CPU cores, improving performance.

'''
import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## create function to compute factorial of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    
    return result


## entry point 
if __name__=="__main__":
    number = [5000,6000,7000,8000]
    
    start_time = time.time()
    
    ## create a pool of worker processes
    with multiprocessing.Pool() as pool:
        result = pool.map(compute_factorial,number)
        
    end_time = time.time()
    
    print(f"Results: {result}")
    print(f"Time Taken: {end_time-start_time} seconds")