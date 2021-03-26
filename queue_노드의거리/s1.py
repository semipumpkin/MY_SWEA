import sys
sys.stdin = open("input.txt", "r")

def bfs(start):
    Q = [start]
    visited = [0] * (V+1)
    visited[start] = 1
    distance = 0
    while Q:
        size = len(Q)
        for i in range(size):
            cur = Q.pop(0)
            if cur == G:
                return distance

            for k in range(1, V+1):
                if visited[k] == False and matrix[cur][k]:
                    Q.append(k)
                    visited[k] = True


        distance += 1
    return 0

def bfs1(start):
    Q = [start]
    visited = [0] * (V+1)
    visited[start] = 0
    while Q:
        cur = Q.pop(0)
        if cur == G:
            return visited[cur]

        for k in range(1, V+1):
            if visited[k] == False and matrix[cur][k]:
                Q.append(k)
                visited[k] = visited[cur] + 1
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        R, C = map(int, input().split())
        matrix[R][C] = 1
        matrix[C][R] = 1
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, bfs1(S)))
    # visited = [[0] * (V + 1)]
    # print(visited)