import subprocess
import os
import sys
sys.path.append(os.getcwd())
from benchmark.b01_stream_read.task import task_definition


def main():
    print(task_definition())


if __name__ == '__main__':
    main()


# p = subprocess.run(["ls", "-ltr"], capture_output=True)
# print(p.stdout.decode(), p.stderr.decode())