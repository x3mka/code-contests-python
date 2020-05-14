def ri(): return int(input())
def ria(): return list(map(int, input().split()))


# dynamic programming down-up
def main():
    for _ in range(ri()):
        n = ri()
        s = ria()
        d = [1] * (n+1)

        for i in range(1, n+1):
            for j in range(2, n//i+1):
                if s[i-1] < s[i*j-1]:
                    d[i*j] = max(d[i*j], d[i]+1)
        print(max(d))


if __name__ == '__main__':
    main()
