import time
import dask
from dask.diagnostics import ProgressBar


names = ['Alice', 'Bob', 'Charles']


def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        time_taken = time.time() - start
        print("{0} {1}".format(func.__name__, time_taken))
    return wrapper


@dask.delayed
def hello_name(name):
    time.sleep(1)
    return 'Hello' + name


# parallel run
@log_time
def run_parallel():
    results = []
    p_steps = [hello_name(name) for name in names]
    results.append(p_steps)
    print(results)
    with ProgressBar():
        output = dask.compute(*results)
    print(output)


run_parallel()
