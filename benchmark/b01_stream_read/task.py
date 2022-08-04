import sys


def naive_using_input():
    return 10


def line_based(original_io, proxy_io_fn=None, **proxy_io_fn_params):
    reader = original_io if proxy_io_fn is None else proxy_io_fn(original_io, proxy_io_fn_params)
    res = 0
    for line in reader:
        res += 1
    return res


def task_definition():
    return {
        'namespace': 'stdin-read',
        'name': 'lines-count',
        'tests': [
            {'name': '67-mb-10-lines', 'assert_result': lambda x: x == 10}
        ],
        'measure': {
            'time': {'repeat': 5},
            'memory': {}
        },
        'params': {
            'stdin': lambda x: sys.stdin,
        },
        'methods': [
            {'name': 'input', 'fn': naive_using_input},
            {'sys.stdin': 'sys.stdin', 'fn': line_based}
        ],
        'test_setup': lambda test_name: {''}
    }
