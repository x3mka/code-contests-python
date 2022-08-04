def char_bytes_to_i(b):
    i = 0
    n = len(b)
    if b[i] == b'-'[0]:
        sign = -1
        i += 1
    else:
        sign = 1
    res = 0
    while i < n:
        res = 10 * res + b[i]-b'0'[0]
        i += 1
    return res if sign == 1 else -res