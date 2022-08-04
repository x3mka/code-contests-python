def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(a, b, c, d):
    if a <= b:
        return b

    slept = b
    left = a - b
    if c <= d:
        return -1
    cycle = c - d

    needed_cycles = left // cycle
    if left % cycle > 0:
        needed_cycles += 1

    return slept + needed_cycles * c


def main():
    for _ in range(ri()):
        a, b, c, d = ria()
        print(solve(a, b, c, d))


if __name__ == '__main__':
    main()
