def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(x1, y1, x2, y2):
    return (x2-x1)*(y2-y1)+1


def main():
    for _ in range(ri()):
        x1, y1, x2, y2 = ria()
        print(solve(x1, y1, x2, y2))


if __name__ == '__main__':
    main()
