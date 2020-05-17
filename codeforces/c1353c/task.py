def ri(): return int(input())
def ria(): return list(map(int, input().split()))


def solve(n):
    k = n // 2
    s = 0
    for i in range(1,k+1):
        s += i*i + (k-i)*(k+i+1) // 2
    return 4 * (s + k*(k+1)//2)


def main():
    for _ in range(ri()):
        n = ri()
        print(solve(n))


if __name__ == '__main__':
    main()
