def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


from itertools import chain, combinations


def solve(s):
    n = len(s)
    ans = n+1

    i = 0
    while i < n:
        d = {}
        j = i
        while j < n and len(d) < 3:
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            j += 1
        if len(d) == 3:
            while i < j and s[i] in d and d[s[i]] > 1:
                d[s[i]] -= 1
                i += 1
            ans = min(ans, j - i)
        i = j

    return 0 if ans == n+1 else ans


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def solve1(s):
    n = len(s)
    ans = n+1

    d = {}
    sets = list([set(st) for st in powerset(['1', '2', '3'])])

    for c in sets:
        if len(c) == 0:
            continue
        key = ''.join(sorted(c))
        d[key] = []
        if len(c) == 1:
            d[key].append(1 if s[0] == key else None)
            for i in range(1, n):
                d[key].append(1 if s[i] == key else (None if d[key][i-1] is None else d[key][i-1]+1))
        else:
            d[key].append(None)
            for i in range(1, n):
                if s[i] in c:
                    s_key = ''.join(sorted(c.difference(s[i])))
                    d[key].append(None if d[s_key][i-1] is None else d[s_key][i-1]+1)
                else:
                    d[key].append(None if d[key][i-1] is None else d[key][i-1]+1)

    for i in range(n):
        if d['123'][i] is not None:
            ans = min(ans, d['123'][i])
    return 0 if ans == n+1 else ans



def main():
    for _ in range(ri()):
        s = rs()
        print(solve1(s))


if __name__ == '__main__':
    main()
