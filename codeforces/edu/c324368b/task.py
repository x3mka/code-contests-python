import sys


def rs(): return sys.stdin.readline().rstrip()


def ri(): return int(sys.stdin.readline())


def ria(): return list(map(int, sys.stdin.readline().split()))


def ws(s): sys.stdout.write(s + '\n')


def wi(n): sys.stdout.write(str(n) + '\n')


def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def pref_sum(n, a):
    b = [[[[[0 for i4 in range(n[4] + 1)] for i3 in range(n[3] + 1)] for i2 in range(n[2] + 1)] for i1 in
          range(n[1] + 1)] for i0 in range(n[0] + 1)]

    for i0 in range(n[0]):
        for i1 in range(n[1]):
            for i2 in range(n[2]):
                for i3 in range(n[3]):
                    for i4 in range(n[4]):
                        b[i0 + 1][i1 + 1][i2 + 1][i3 + 1][i4 + 1] = (
                                + b[i0][i1][i2][i3][i4]
                                - b[i0][i1][i2][i3][i4 + 1]
                                - b[i0][i1][i2][i3 + 1][i4]
                                - b[i0][i1][i2 + 1][i3][i4]
                                - b[i0][i1 + 1][i2][i3][i4]
                                - b[i0 + 1][i1][i2][i3][i4]
                                + b[i0][i1][i2][i3 + 1][i4 + 1]
                                + b[i0][i1][i2 + 1][i3][i4 + 1]
                                + b[i0][i1][i2 + 1][i3 + 1][i4]
                                + b[i0][i1 + 1][i2][i3][i4 + 1]
                                + b[i0][i1 + 1][i2][i3 + 1][i4]
                                + b[i0][i1 + 1][i2 + 1][i3][i4]
                                + b[i0 + 1][i1][i2][i3][i4 + 1]
                                + b[i0 + 1][i1][i2][i3 + 1][i4]
                                + b[i0 + 1][i1][i2 + 1][i3][i4]
                                + b[i0 + 1][i1 + 1][i2][i3][i4]
                                - b[i0][i1][i2 + 1][i3 + 1][i4 + 1]
                                - b[i0][i1 + 1][i2][i3 + 1][i4 + 1]
                                - b[i0][i1 + 1][i2 + 1][i3][i4 + 1]
                                - b[i0][i1 + 1][i2 + 1][i3 + 1][i4]
                                - b[i0 + 1][i1][i2][i3 + 1][i4 + 1]
                                - b[i0 + 1][i1][i2 + 1][i3][i4 + 1]
                                - b[i0 + 1][i1][i2 + 1][i3 + 1][i4]
                                - b[i0 + 1][i1 + 1][i2][i3][i4 + 1]
                                - b[i0 + 1][i1 + 1][i2][i3 + 1][i4]
                                - b[i0 + 1][i1 + 1][i2 + 1][i3][i4]
                                + b[i0][i1 + 1][i2 + 1][i3 + 1][i4 + 1]
                                + b[i0 + 1][i1][i2 + 1][i3 + 1][i4 + 1]
                                + b[i0 + 1][i1 + 1][i2][i3 + 1][i4 + 1]
                                + b[i0 + 1][i1 + 1][i2 + 1][i3][i4 + 1]
                                + b[i0 + 1][i1 + 1][i2 + 1][i3 + 1][i4]
                                + a[i0][i1][i2][i3][i4]
                        )
    return b


def query(b, l0, l1, l2, l3, l4, r0, r1, r2, r3, r4):
    return (
            - b[l0][l1][l2][l3][l4]
            + b[l0][l1][l2][l3][r4]
            + b[l0][l1][l2][r3][l4]
            + b[l0][l1][r2][l3][l4]
            + b[l0][r1][l2][l3][l4]
            + b[r0][l1][l2][l3][l4]
            - b[l0][l1][l2][r3][r4]
            - b[l0][l1][r2][l3][r4]
            - b[l0][l1][r2][r3][l4]
            - b[l0][r1][l2][l3][r4]
            - b[l0][r1][l2][r3][l4]
            - b[l0][r1][r2][l3][l4]
            - b[r0][l1][l2][l3][r4]
            - b[r0][l1][l2][r3][l4]
            - b[r0][l1][r2][l3][l4]
            - b[r0][r1][l2][l3][l4]
            + b[l0][l1][r2][r3][r4]
            + b[l0][r1][l2][r3][r4]
            + b[l0][r1][r2][l3][r4]
            + b[l0][r1][r2][r3][l4]
            + b[r0][l1][l2][r3][r4]
            + b[r0][l1][r2][l3][r4]
            + b[r0][l1][r2][r3][l4]
            + b[r0][r1][l2][l3][r4]
            + b[r0][r1][l2][r3][l4]
            + b[r0][r1][r2][l3][l4]
            - b[l0][r1][r2][r3][r4]
            - b[r0][l1][r2][r3][r4]
            - b[r0][r1][l2][r3][r4]
            - b[r0][r1][r2][l3][r4]
            - b[r0][r1][r2][r3][l4]
            + b[r0][r1][r2][r3][r4]
    )


def read_array(n):
    a = [[[[[0 for i4 in range(n[4] + 1)] for i3 in range(n[3] + 1)] for i2 in range(n[2] + 1)] for i1 in
          range(n[1] + 1)] for i0 in range(n[0] + 1)]

    for i0 in range(n[0]):
        for i1 in range(n[1]):
            for i2 in range(n[2]):
                for i3 in range(n[3]):
                    a[i0][i1][i2][i3] = ria()
    return a


def main():
    n = ria()
    a = read_array(n)

    b = pref_sum(n, a)

    q = ri()
    for i in range(q):
        l1, l2, l3, l4, l5, r1, r2, r3, r4, r5 = ria()
        wi(query(b, l1 - 1, l2 - 1, l3 - 1, l4 - 1, l5 - 1, r1, r2, r3, r4, r5))


if __name__ == '__main__':
    main()
