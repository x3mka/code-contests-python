import os
import sys
sys.path.append(os.getcwd())
from benchmark.utils import track_memory, track_time
from benchmark.b01_stream_read.utils import big_file_stream
import mmap


@track_memory
@track_time
def benchmark(f):
    with mmap.mmap(f.fileno(), 0) as mapped:
        res = 0
        for line in mapped:
            res += len(line)
            # res += len(line.split())
            # res += sum([int(s) for s in line.split()])
    return res


if __name__ == '__main__':
    with big_file_stream() as bfs:
        result = benchmark(bfs)
        print("Result: {}".format(result))

