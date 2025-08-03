import time
from functools import wraps

def inspector(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'depth'):
            wrapper.depth = 0
        if wrapper.depth == 0:
            start_time = time.time()
        wrapper.depth += 1

        result = func(*args, **kwargs)

        wrapper.depth -= 1
        if wrapper.depth == 0:
            end_time = time.time()
            print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper
