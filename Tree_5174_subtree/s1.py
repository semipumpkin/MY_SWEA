import sys
sys.stdin = open('input.txt', 'r')

def counting(node):
    global count
    if node == 0:
        return
    count += 1
    counting(tree[node][0])
    counting(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0, 0, 0] for _ in range(E + 2)]
    count = 0
    for i in range(E):
        parent = temp[i*2]
        child = temp[i*2 + 1]
        if tree[parent][0]:
            tree[parent][1] = child
        else:
            tree[parent][0] = child
        tree[child][2] = parent
    # print(find_root(1))
    counting(N)
    print('#{} {}'.format(tc, count))