import os


def big_file_stream(file_name='big_file.txt', binary=False):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = cur_dir + '/' + file_name
    if binary:
        return open(test_file, 'rb')
    else:
        return open(test_file, 'r', encoding='utf-8')
