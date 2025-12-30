## Multiprocessing 
# --> It allows  processes that run in parallel

## When to use multiprocessing 

### There are two reasons to use multi processing

# 1- CPU bound Tasks
## Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing)

# 2- Parallel Execution - Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(.5)
        print(f"Square: {i*i}")
        
def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")
        
if __name__=="__main__":    # Entry point
    # Creating two processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t1 = time.time()
    # to start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time()-t1 
    print('Total Time:',finished_time)
