from time import sleep
from concurrent.futures import ThreadPoolExecutor


class MemoryMonitor:
    def __init__(self):
        self.keep_measuring = True

    def measure_usage(self):
        max_usage = 0
        while self.keep_measuring:
            print('Yo!')
            sleep(1)

        return max_usage





def measure_memory(func):
    def wrapper(*args, **kwargs):
        with ThreadPoolExecutor() as executor:
            monitor = MemoryMonitor()
            mem_thread = executor.submit(monitor.measure_usage)
            try:
                fn_thread = executor.submit(func, *args, **kwargs)
                result = fn_thread.result()
            finally:
                monitor.keep_measuring = False
                max_usage = mem_thread.result()

            print(f"Peak memory usage: {max_usage}")
            return result
    return wrapper