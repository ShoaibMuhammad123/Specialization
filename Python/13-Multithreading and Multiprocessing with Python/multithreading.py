## Multi threding

## When to use multithreading
## --> There are two important reasons 
# 1- I/O bound tasks
import threading
import time

def print_numbers():
    for i in range(5):
        print(f'Numbers:{i}')

def print_letter():
    for letter in "abcde":
        print(f"Letter: {letter}")
        
t = time.time()
# print_numbers()
# print_letter()

# finished_time = time.time()-t

# print(finished_time)

### Introduce Sleeping method 

def print_numbers():
    for i in range(5):
        time.sleep(.5)
        print(f'Numbers:{i}')

def print_letter():
    for letter in "abcde":
        time.sleep(.5)
        print(f"Letter: {letter}")
        
# t = time.time()
# print_numbers()
# print_letter()

# finished_time = time.time()-t

# print(finished_time)


### Creating two Threads

def print_numbers():
    for i in range(5):
        time.sleep(.5)
        print(f'Numbers:{i}')

def print_letter():
    for letter in "abcde":
        time.sleep(.5)
        print(f"Letter: {letter}")
        
        

## Create two threads 
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)


t = time.time()
## Start the threads
t1.start()
t2.start()

## It also wait for the threads to complete 
# once it become complete we join the threads in to a new thread
t1.join()
t2.join()

finished_time = time.time()-t

print(finished_time)

## This show that the above function took 5 seconds to execute but, when we use 
#  multithreading it only took 2 seconds
