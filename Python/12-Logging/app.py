import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    ## we can also write filename through handler 
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()        # it is responsible for putting all the log information in this particular file
    ]
)

## now we create a logger
logger = logging.getLogger('ArithmethicApp')   # it is used for my  module
def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b}:= {result}")
    return result


## similarly i am doing this for subtraction as well
def sub(a,b):
    result = a-b
    logger.debug(f"Subtracting {a} - {b}:= {result}")
    return result

def mul(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} x {b}:= {result}")
    return result

def div(a,b):
    try:
        result = a/b  
        logger.debug(f"Dividing {a} / {b}:= {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero Error")
        return None


## Calling 
add(4,5)
sub(5,3)
mul(4,3)
div(5,0)