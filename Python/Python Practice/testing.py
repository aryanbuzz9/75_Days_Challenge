#Timing function execution
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=main_func(*args,**kwargs)
        end=time.time()
        print(f'main_function {end-start}')
        return result
    return wrapper

@timer
def main_func(n):
    time.sleep(n)
main_func(2)