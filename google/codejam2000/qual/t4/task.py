import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n'); sys.stdout.flush()
def wi(n): sys.stdout.write(str(n) + '\n'); sys.stdout.flush()


import time


class ItemPossibilitySet:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    def len(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def is_confident(self):
        return len(self.data) == 1

    def is_not_confident(self):
        return len(self.data) > 1

    def can_have_value(self, val):
        return val in self.data

    def update_intersected(self, ps):
        self.data.intersection_update(ps)

    def first_value(self):
        return next(iter(self.data))

    def copy(self):
        return ItemPossibilitySet([ps.copy() for ps in self.data])


class GuessSet:
    def __init__(self, n, ps=lambda x: {0, 1}, name='i'):
        self.n = n
        self.name = name
        self.data = [ItemPossibilitySet(ps(_)) for _ in range(n)]

        self.bad = set()
        self.confident = set()
        self.not_confident = set()

        for i, ips in enumerate(self.data):
            if ips.is_not_confident():
                self.not_confident.add(i)
            elif ips.is_confident():
                self.confident.add(i)
            else:
                self.bad.add(i)

    def __repr__(self):
        return "GuessSet(confident: {0}, not_confident: {1}, bad: {2}): {3}".format(len(self.confident), len(self.not_confident), len(self.bad), str(self.data))

    def __eq__(self, other):
        res = True
        for i in range(self.n):
            if self.data[i].data != other.data[i].data:
                res = False
                break
        return res

    def hash(self):
        return '$'.join([''.join([str(s) for s in ps.data]) for ps in self.data])

    def is_confident(self):
        return len(self.confident) == self.n

    def is_not_confident(self):
        return len(self.not_confident) > 0

    def is_bad(self):
        return len(self.bad) > 0

    def pick_first_non_confident(self):
        i = next(iter(self.not_confident))
        return i, self.data[i]

    def pick_confident_pair(self):
        # for i in range(self.n):
        #     if i in self.confident and self.n - i - 1 in self.confident and self.data[i].first_value() == self.data[self.n - i - 1].first_value():
        #         return i, self.n - i - 1
        for i in range(self.n):
            if i in self.confident and self.n - i - 1 in self.confident:
                return i, self.n - i - 1
        return None, None

    def pick_non_confident_in_pair(self):
        # paired
        for i in range(self.n):
            if i in self.not_confident and self.n - i - 1 in self.confident:
                return i
        # if no pairs
        for i in range(self.n):
            if i in self.not_confident:
                return i
        return None

    def update_item_intersected(self, i, ps):
        old_len = self.data[i].len()
        self.data[i].update_intersected(ps)
        new_len = self.data[i].len()
        if old_len == 0:
            self.bad.remove(i)
        elif old_len == 1:
            self.confident.remove(i)
        else:
            self.not_confident.remove(i)
        if new_len == 0:
            self.bad.add(i)
        elif new_len == 1:
            self.confident.add(i)
        else:
            self.not_confident.add(i)

    def answer(self, skip_confidence_check=False):
        if not skip_confidence_check:
            assert self.is_confident()
        return ''.join([str(s.first_value()) for s in self.data])

    def copy_as_same(self):
        ps = GuessSet(self.n, name=self.name+'i')
        for i in range(self.n):
            ps.update_item_intersected(i, self.data[i].data.copy())
        return ps

    def copy_as_complement(self):
        ps = GuessSet(self.n, name=self.name+'c')
        for i in range(self.n):
            s = set()
            for si in self.data[i].data:
                s.add(1 - si)
            ps.update_item_intersected(i, s)
        return ps

    def copy_as_reversed(self):
        ps = GuessSet(self.n, name=self.name+'r')
        for i in range(self.n):
            ps.update_item_intersected(i, self.data[self.n - i - 1].data.copy())
        return ps

    def copy_as_both(self):
        ps = GuessSet(self.n, name=self.name+'b')
        for i in range(self.n):
            s = set()
            for si in self.data[self.n - i - 1].data:
                s.add(1 - si)
            ps.update_item_intersected(i, s)
        return ps


class Strategy:

    def __init__(self, n, debug=False, is_logging=False):
        self.n = n
        self.debug = debug
        self.sets = [self.new_ps()]
        self.idx = 0

        self.is_logging = is_logging
        self.log_file = open('log.txt', 'w') if is_logging else None

    def __del__(self):
        if self.is_logging:
            self.log_file.close()

    def log(self, s):
        if self.is_logging:
            t = time.time()
            self.log_file.write(str(t) + ": ")
            self.log_file.write(s)
            self.log_file.write("\n")

    def __repr__(self):
        return "Strategy(step={0}, sets={1})".format(self.idx, len(self.sets))
        # return "Strategy(step={0}, sets={1}): {2}".format(self.idx, len(self.sets), str(self.sets))

    def is_confident(self):
        for s in self.sets:
            if not s.is_confident():
                return False
        return len(self.sets) == 1

    def merge_sets(self):
        if len(self.sets) <= 1:
            return

        d = {}
        for i in range(len(self.sets)):
            h = self.sets[i].hash()
            if h not in d:
                d[h] = [i]
            else:
                d[h].append(i)

        self.log("Hashes:" + str(d))

        ss = []
        for h, ii in d.items():
            ss.append(self.sets[ii[0]])

        if len(ss) != len(self.sets):
            self.log("Merged: {0} -> {1}".format(len(self.sets), len(ss)))
            self.sets = ss

    def answer(self):
        return self.sets[0].answer()

    def new_ps(self):
        return GuessSet(self.n)

    def pick_confident_pair(self):
        for s in self.sets:
            res = s.pick_confident_pair()
            if res is not None:
                return res
        return None

    def pick_non_confident_in_pair(self):
        for s in self.sets:
            res = s.pick_non_confident_in_pair()
            if res is not None:
                return res
        return None

    def pick_differing_bit(self):
        for i in range(self.n):
            val = self.sets[0].data[i].first_value()
            for s in self.sets:
                s_val = s.data[i].first_value()
                if s_val != val:
                    return i
        return None

    def ask(self, i):
        # self.log("Asking bit: {0}".format(i+1))
        self.idx += 1
        wi(i + 1)
        return ri()

    def step_fluctuations(self):
        if self.debug:
            ws("Step: fluctuation bit test")
        candidates = []
        for s in self.sets:
            candidates += [
                s.copy_as_same(),
                s.copy_as_complement(),
                s.copy_as_reversed(),
                s.copy_as_both()
            ]
        pair = self.pick_confident_pair()

        if pair is None:
            self.ask(0)
        else:
            s_bit, e_bit = pair
            s_val = self.ask(s_bit)
            e_val = self.ask(e_bit)

            possible = []
            for s in candidates:
                if s.data[s_bit].can_have_value(s_val) and s.data[e_bit].can_have_value(e_val):
                    possible.append(s)
            self.sets = possible
        self.merge_sets()

    def step_bit_test(self):
        if self.debug:
            ws("Step: bit test")
        # here we need to pick best bit index to ask
        # bit = self.pick_non_confident_in_pair()
        # if bit is None:
        bit = self.pick_differing_bit()
        if bit is None:
            bit = self.pick_non_confident_in_pair()
        response = self.ask(bit)
        for i in range(len(self.sets)-1, -1, -1):
            s = self.sets[i]
            s.update_item_intersected(bit, {response})
            if s.is_bad():
                self.sets.remove(s)

    def step(self):
        if self.idx > 0 and self.idx % 10 == 0:
            return self.step_fluctuations()
        else:
            return self.step_bit_test()

    def run(self):
        self.log(str(self))
        while not self.is_confident() and self.idx < 150:
            self.step()
            if self.debug:
                ws(str(self))
            # self.log("Step: {0}, sets: {1}".format(self.idx, len(self.sets)))
            self.log(str(self))
        ws(self.answer())
        response = rs()
        return True if response == 'Y' else False


def solve(b):
    s = Strategy(b, debug=False, is_logging=False)
    return s.run()


def main():
    t, b = ria()
    for _ in range(t):
        if not solve(b):
            exit()


if __name__ == '__main__':
    main()
