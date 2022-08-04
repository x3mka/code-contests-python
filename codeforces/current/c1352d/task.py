def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(n, a):
    moves = 0
    cur_player = 0
    idx = [0, n-1]
    vols = [0, 0]
    total = [0, 0]
    d = 1

    while idx[1] >= idx[0]:
        other_player = (cur_player + 1) % 2
        vols[cur_player] = 0
        while vols[cur_player] <= vols[other_player] and idx[1] >= idx[0]:
            vols[cur_player] += a[idx[cur_player]]
            idx[cur_player] += d
        total[cur_player] += vols[cur_player]
        moves += 1
        d = -d
        cur_player = other_player
    return [moves] + total


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        print(ia_to_s(solve(n, a)))


if __name__ == '__main__':
    main()
