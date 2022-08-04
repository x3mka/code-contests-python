from binarytree import Node
from collections import deque


def bin_count(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n &= (n - 1)
    return cnt


def test(n=6):
    masks = set([_ for _ in range(1 << n)])

    root = Node(0)
    q = deque([root])
    while q:
        node = q.popleft()
        masks.remove(node.value)
        for mask in masks:
            if (mask ^ (1 << (n - bin_count(mask)))) == node.value:
                new_node = Node(mask)
                q.append(new_node)
                if node.left:
                    node.right = new_node
                else:
                    node.left = new_node

    print(root)


if __name__ == '__main__':
    test()
