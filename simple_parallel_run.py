import time
from dask import delayed
import dask


names = ['Alice', 'Bob', 'Charles']


def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        time_taken = time.time() - start
        print("{0} {1}".format(func.__name__, time_taken))
    return wrapper


def hello_name(name):
    time.sleep(1)
    return 'Hello' + name


# sequential run
@log_time
def run_sequential():
    for name in names:
        hello_name(name)


run_sequential()


# defining the parallize function
def parallize(function_name, somelist):
    p_steps = [delayed(function_name)(name) for name in somelist]
    futures = dask.persist(*p_steps)
    dask.compute(*futures)


# parallel run
@log_time
def run_parallel():
    parallize(hello_name, names)


run_parallel()
