import sys
sys.stdin = open('input.txt', 'r')

def in_order(node):
    if node:
        in_order(temp[node][0])
        print(temp[node][-1], end='')
        in_order(temp[node][1])
for tc in range(1, 11):
    V = int(input())

    temp = [[0, 0, 0, ''] for _ in range(V + 1)]
    for i in range(1, V + 1):
        info = list(input().split())
        temp[i][-1] += info[1]
        temp[i][2] = int(info[0])
        if len(info) == 3:
            temp[i][0] = int(info[2])
        elif len(info) == 4:
            temp[i][0] = int(info[2])
            temp[i][1] = int(info[3])
    print(f'#{tc}', end=' ')
    in_order(1)
    print()



