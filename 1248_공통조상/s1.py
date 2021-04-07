import sys
sys.stdin = open('input.txt', 'r')



def volume(nod):
    global count
    if nod == 0:
        return

    count += 1
    volume(tree[nod][0])
    volume(tree[nod][1])


# 조상찾는 함수
def find_parent(node, arr):
    # 정점일때 끝남
    if node == 0:
        return
    else:
        arr.append(node)
        find_parent(tree[node][2], arr)
# 후위순회?

T = int(input())
for tc in range(1, T+1):
    V, E, v1, v2 = map(int, input().split())
    temp = list(map(int, input().split()))
    # print(V, E, v1, v2)
    # print(temp)
    tree = [[0, 0, 0] for _ in range(V+1)]

    for i in range(E):
        parent = temp[2*i]
        child = temp[2*i+1]
        if tree[parent][0]:
            tree[parent][1] = child
        else:
            tree[parent][0] = child
        tree[child][2] = parent


    v1_tree = []
    v2_tree = []

    find_parent(v1, v1_tree)
    find_parent(v2, v2_tree)
    print(v1_tree, v2_tree)

    for node in v1_tree:
        if node in v2_tree:
            count = 0
            volume(node)
            print(f'#{tc} {node} {count}')
            break
