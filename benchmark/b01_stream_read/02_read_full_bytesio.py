import os
import sys
sys.path.append(os.getcwd())
from benchmark.utils import track_memory, track_time
from benchmark.b01_stream_read.utils import big_file_stream
from memory_profiler import profile
import io


def by_line_full_stream_reader(f):
    return io.BytesIO(os.read(f.fileno(), os.fstat(f.fileno()).st_size))  #.readline


@track_time
@profile
# @track_memory
def benchmark(f):
    reader = by_line_full_stream_reader(f)
    # return sum(list(map(lambda x: len(x.split(b' ')), reader)))

    res = 0
    for line in reader:
        # res += 1
        res += len(line.rstrip(b'\n'))
        # res += sum([char_bytes_to_i(x) for x in line.rstrip().split(b' ')])
        # print(line.rstrip().split(b' ')[-1])
    return res


if __name__ == '__main__':
    with big_file_stream(binary=True) as bfs:
        result = benchmark(bfs)
        print("Result: {}".format(result))

