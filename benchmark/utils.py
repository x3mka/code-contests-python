import tracemalloc
import timeit
import os
import psutil


def track_memory(func):
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        before_mb = process.memory_info().rss / 1024 ** 2
        result = func(*args, **kwargs)
        after_mb = process.memory_info().rss / 1024 ** 2
        print("Max memory used: {0:.02f} MB, before start: {1:.02f} MB".format(after_mb, before_mb))
        return result
    return wrapper


def track_memory1(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print("Max memory used: {0:.02f} MB".format(peak / 1024 ** 2))
        return result
    return wrapper


def track_time(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed_time = timeit.default_timer() - start
        print("Exec time: {0:.2f} secs".format(elapsed_time))
        return result
    return wrapper
