import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


class Pattern:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"

    def matchPrefIndices(self, s, sl):
        raise NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False


class CharPattern(Pattern):
    def __init__(self, char):
        super().__init__(char)

    def matchPrefIndices(self, s):
        if len(s) > 0 and s[0] == self.id:
            return [1]
        return []


class CharsPattern(Pattern):
    def __init__(self, char):
        super().__init__(char + '*')

    def matchPrefIndices(self, s):
        res = [0]
        n = len(s)
        i = 0
        while i < n and s[i] == self.id[0]:
            res.append(i + 1)
            i += 1
        return res


class AnyCharPattern(Pattern):
    def __init__(self):
        super().__init__('.')

    def matchPrefIndices(self, s):
        if s:
            return [1]
        return []


class AnyCharsPattern(Pattern):
    def __init__(self):
        super().__init__('.*')

    def matchPrefIndices(self, s):
        return list(range(len(s) + 1))


class Solution:
    def buildPatterns(self, p: str):
        patterns = []

        while p:
            m = len(p)
            try:
                i = p.index('*')
            except ValueError:
                i = m + 1

            for j in range(i - 1):
                if p[j] == '.':
                    patterns.append(AnyCharPattern())
                else:
                    patterns.append(CharPattern(p[j]))

            if i < m:
                if p[i - 1] == '.':
                    patterns.append(AnyCharsPattern())
                else:
                    patterns.append(CharsPattern(p[i - 1]))

            p = p[i + 1:]

        compressed = [patterns[0]]
        for i in range(1, len(patterns)):
            if isinstance(patterns[i], AnyCharsPattern) and isinstance(patterns[i - 1], AnyCharsPattern):
                continue
            if isinstance(patterns[i], CharsPattern) and isinstance(patterns[i - 1], CharsPattern) and patterns[i].id == \
                    patterns[i - 1].id:
                continue
            compressed.append(patterns[i])

        return compressed

    def match(self, s, patterns):
        n = len(s)
        m = len(patterns)
        if n == 0 and m == 0:
            return True
        if n > 0 and m == 0:
            return False
        if n == 0 and m > 0:
            return all([isinstance(p, AnyCharsPattern) or isinstance(p, CharsPattern) for p in patterns])

        if (isinstance(patterns[0], CharPattern) or isinstance(patterns[0], AnyCharPattern)):
            indices = patterns[0].matchPrefIndices(s)
            if not indices:
                return False
            return any([self.match(s[j:], patterns[1:]) for j in indices])

        if (isinstance(patterns[-1], CharPattern) or isinstance(patterns[-1], AnyCharPattern)):
            indices = patterns[-1].matchPrefIndices(s[::-1])
            if not indices:
                return False
            return any([self.match(s[:n-j], patterns[:-1]) for j in indices])

        if (isinstance(patterns[0], CharsPattern)):
            indices = patterns[0].matchPrefIndices(s)
            if not indices:
                return False
            return any([self.match(s[j:], patterns[1:]) for j in indices])

        if (isinstance(patterns[-1], CharsPattern)):
            indices = patterns[-1].matchPrefIndices(s[::-1])
            if not indices:
                return False
            return any([self.match(s[:n-j], patterns[:-1]) for j in indices])

        indices = patterns[0].matchPrefIndices(s)
        if not indices:
            return False
        return any([self.match(s[j:], patterns[1:]) for j in indices])

    def isMatch(self, s: str, p: str) -> bool:
        patterns = self.buildPatterns(p)
        # print(patterns)
        return self.match(s, patterns)


def solve(s, p):
    sol = Solution()
    res = sol.isMatch(s, p)
    return 'true' if res else 'false'


def main():
    s = rs()
    p = rs()

    ws(solve(s, p))


if __name__ == '__main__':
    main()
