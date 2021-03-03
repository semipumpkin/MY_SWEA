import sys
sys.stdin = open("input.txt", "r")

# dfs 함수에 리스트를 넣을때도 구현해보자
def dfs(s, e):
    visited = [0] * (V+1)
    stack = []
    stack.append(s)
    while len(stack):
        top = stack.pop()
        if e in arrays[top]:
            return 1
        if visited[top] == 0:
            visited[top] = 1
        for w in range(len(arrays[top])):
            if visited[arrays[top][w]] == 0:
                stack.append(arrays[top][w])
                visited[arrays[top][w]] = 1
    return 0
T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arrays = [[] for _ in range(V+1)]

    for _ in range(E):
        y, x = map(int, input().split())

        arrays[y].append(x)

    start, end = map(int, input().split())
    print('#{} {}'.format(tc, dfs(start, end)))
    # print(arrays)