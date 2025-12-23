from logger import logging

def add(a,b):
    logging.debug('The addtion operation is being taking place')
    return a+b
  
logging.debug('The addtion function is  called')  
result = add(3,4)
print(result)