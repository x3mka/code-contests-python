import os
import sys
sys.path.append(os.getcwd())
from benchmark.utils import track_memory, track_time, track_memory1
from benchmark.b01_stream_read.utils import big_file_stream
from memory_profiler import profile


@profile
# @track_memory1
# @track_time
def benchmark(f):
    # return sum(list(map(lambda x: len(x.split()), f)))
    res = 0
    for line in f:
        # res += 1
        res += len(line)
        # res += len(line.split())
        # res += sum([int(s) for s in line.split()])
        # print(line.split()[-1])
    return res


if __name__ == '__main__':
    with big_file_stream() as bfs:
        result = benchmark(bfs)
        print("Result: {}".format(result))

