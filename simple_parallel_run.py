import time
import dask
from dask import delayed

names = ['Alice', 'Bob', 'Charles']


def hello_name(name):
    time.sleep(1)
    return 'Hello' + name

# sequential run
start = time.time()
for name in names:
    hello_name(name)
time_taken = time.time() - start
print('    Sequential process for took %0.2f seconds' % time_taken)

# parallel run
start = time.time()
p_steps = [delayed(hello_name)(name) for name in names]
futures = dask.persist(*p_steps)
dask.compute(*futures)
time_taken = time.time() - start
print('    Parallel process for took %0.2f seconds' % time_taken)
