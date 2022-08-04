import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


import heapq


def main():
    n = ri()
    a = []

    for i in range(n):
        a.append(ria() + [i])

    a.sort(key=lambda x: (x[1], x[0]))

    rooms = []
    res = [0] * n

    for i in range(n):
        if rooms and rooms[0][0] < a[i][0]:
            num = rooms[0][1]
            heapq.heappushpop(rooms, (a[i][1], num))
            res[a[i][2]] = num
        else:
            num = len(rooms) + 1
            heapq.heappush(rooms, (a[i][1], num))
            res[a[i][2]] = num

    wi(len(rooms))
    wia(res)


if __name__ == '__main__':
    main()
