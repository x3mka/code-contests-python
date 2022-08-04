import random
import os


def generate(file_name='big_file', use_ascii=False):
    encoding = 'ascii' if use_ascii else 'utf-8'
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = cur_dir + '/' + file_name + '_' + encoding + '.txt'

    n = 10000000
    start = 100000
    end = 999999
    per_line = 1000000
    count_in_line = 0

    with open(test_file, 'w', encoding=encoding) as f:
        for i in range(n):
            a = random.randrange(start, end)
            if count_in_line > 0:
                f.write(' ')
            f.write(str(a))
            count_in_line += 1
            if count_in_line == per_line:
                f.write('\n')
                count_in_line = 0


if __name__ == '__main__':
    generate()
