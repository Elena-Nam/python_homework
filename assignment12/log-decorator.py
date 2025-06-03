import logging

# Task 1 

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
logger.log(logging.INFO, "this string would be logged")

def logger_decorator(func):
    def wrapper(*args, **kwargs):
         # Format positional parameters
        pos_params = list(args) if args else "none"
        # Format keyword parameters
        kw_params = kwargs if kwargs else "none"

        result = func(*args, **kwargs)
        
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {kw_params}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "") 

        return result
    return wrapper

# 1.3
@logger_decorator
def no_parameters():
    print("Hello World!")

# 1.4
@logger_decorator
def with_posit_arguments(*args):
    return True

# 1.5
@logger_decorator
def no_posit_parameters(**kwargs):
    return logger_decorator

# 1.6
no_parameters()
with_posit_arguments(1, 2, 3)
no_posit_parameters(key1="value1", key2="value2")