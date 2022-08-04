def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(s):
    n = len(s)
    s = [int(si) for si in s]
    ones = sum(s)
    zeros = n - ones

    ans = n
    ones_i = 0
    zeros_i = 0
    for i in range(0, n):
        if s[i] == 1:
            ones_i += 1
        if s[i] == 0:
            zeros_i += 1

        # converting to 1111000000
        # to convert left [:i] to all ones: zeros_i
        # to convert right [i+1:] to all zeros: ones - ones_i
        m1 = zeros_i + ones - ones_i

        # converting to 0000011111
        # to convert left [:i] to all zeros: ones_i
        # to convert right [i+1:] to all ones: zeros - zeros_i
        m2 = ones_i + zeros - zeros_i

        ans = min(ans, m1, m2)

    return ans


def main():
    for _ in range(ri()):
        s = rs()
        print(solve(s))


if __name__ == '__main__':
    main()
