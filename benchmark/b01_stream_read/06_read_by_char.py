import os
import sys
sys.path.append(os.getcwd())
from benchmark.utils import track_memory, track_time
from benchmark.b01_stream_read.utils import big_file_stream
import io


import gc
import os



def fast_num_reader(f, sep=b' ', chunk_size=8*1024):
    i = 0
    cur = b''
    while True:
        chunk = f.read(chunk_size)
        if chunk == b'':
            yield cur
            break
        while True:
            i = chunk.find(sep)
            if i == -1:
                break
            yield cur + chunk[:i]
            cur = b''
            chunk = chunk[i+1:]

    while data:
        c = data[i]
        if c == b'-'[0]:
            x = 0
            sign = 1
        else:
            x = c - b'0'[0]
            sign = 0
        c = next(ch_reader)
        while c >= b'0'[0]:
            x = 10 * x + c - b'0'[0]
            c = next(ch_reader)
        if c == b'\r'[0]:
            next(ch_reader)
        yield -x if sign else x

        data = os.read(fd, chunk_size)


# @track_memory
@track_time
def benchmark(f):
    reader = fast_num_reader(f)

    res = 0
    for num in reader:
        # res += 1
        res += num
        # print(line.rstrip().split(b' ')[-1])
    return res


if __name__ == '__main__':
    with big_file_stream(binary=True) as bfs:
        result = benchmark(bfs)
        print("Result: {}".format(result))

