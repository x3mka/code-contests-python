import os
import sys
sys.path.append(os.getcwd())
from benchmark.utils import track_memory, track_time
from benchmark.b01_stream_read.utils import big_file_stream
import io


def by_line_buffered_stream_reader(f, chunk_size=20 * 1024**2):
    size = os.fstat(f.fileno()).st_size

    data = io.BytesIO(f.read(chunk_size))
    total = data.getbuffer().nbytes
    while total < size:
        yield from data
        data = io.BytesIO(f.read(chunk_size))
        total += data.getbuffer().nbytes


def buffered_reader(f, chunk_size=20*1024**2):
    lines = f.readlines(chunk_size)
    while lines:
        yield from lines
        lines = f.readlines(chunk_size)


@track_memory
@track_time
def benchmark(f):
    reader = by_line_buffered_stream_reader(f)

    res = []
    for line in reader:
        # res += 1
        res.append(len(line))
        # res += len(line.split(b' '))
    # while line != b'':
    #     res += len(line.split(b' '))
    #     line = read_line()
    return res


if __name__ == '__main__':
    with big_file_stream(binary=True) as bfs:
        result = benchmark(bfs)
        print("Result: {}".format(result))

