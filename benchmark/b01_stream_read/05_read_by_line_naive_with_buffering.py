import os
import sys
sys.path.append(os.getcwd())
from benchmark.utils import track_memory, track_time
from benchmark.b01_stream_read.utils import big_file_stream


def buffered_reader(f, chunk_size=30*1024**2):
    lines = f.readlines(chunk_size)
    while lines:
        yield from lines
        lines = f.readlines(chunk_size)




@track_memory
@track_time
def benchmark(f):
    # return sum(list(map(lambda x: len(x.split()), f)))

    reader = buffered_reader(f)

    res = 0
    for line in reader:
        res += 1
        # res += len(line)
        # res += len(line.split())
        # res += sum([int(s) for s in line.split()])
    return res


if __name__ == '__main__':
    with big_file_stream() as bfs:
        result = benchmark(bfs)
        print("Result: {}".format(result))

