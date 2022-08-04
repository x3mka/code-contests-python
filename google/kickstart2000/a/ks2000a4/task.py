import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a])); sys.stdout.write('\n')

from collections import deque


class TrieNode(object):
    """Trie node implementation."""
    def __init__(self, char: str):
        self.char = char
        self.children = {}
        self.finished_words_count = 0
        self.count = 1

    def __repr__(self):
        return "TrieNode({0}: {1})".format(self.char, str(list(self.children.keys())))

    def add(self, word):
        """Adding a word"""
        node = self
        node.count += 1
        for char in word:
            if char in node.children:
                child = node.children[char]
                child.count += 1
                node = child
            else:
                child = TrieNode(char)
                node.children[char] = child
                node = child
        node.finished_words_count += 1


class Trie:
    def __init__(self, words):
        self.root = TrieNode('*')
        for word in words:
            self.add(word)

    def __repr__(self):
        return "Trie({0})".format(self.root)

    def add(self, word):
        self.root.add(word)

    def do(self, k):
        q = deque()
        q.append(self.root)

        ans = 0
        while q:
            node = q.popleft()
            if node.char != '*':
                ans += node.count // k
            for ch in node.children.values():
                q.append(ch)
        return ans


def solve(n, k, s):
    t = Trie(s)
    return t.do(k)


def main():
    for t in range(ri()):
        n, k = ria()
        s = []
        for _ in range(n):
            s.append(rs())
        ws("Case #{}: {}".format(t+1, solve(n, k, s)))


if __name__ == '__main__':
    main()
