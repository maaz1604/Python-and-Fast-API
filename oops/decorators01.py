import time

def timer(func):
    def wrapper(*args,**kwargs):
        startTime = time.time()
        result = func(*args,**kwargs)
        endTime = time.time()
        print(f'{func.__name__} ran in {endTime} time')
        return result
    return wrapper

@timer
def example(n):
    time.sleep(n)
    
example(2)