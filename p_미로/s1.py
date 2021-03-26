import sys
sys.stdin = open("input.txt", "r")


def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []
    # 시작점 넣어주고
    stack.append([y, x])
    # 방문 리스트 및 방문체크
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1

    # 스택이 빌때까지
    while stack:

        V = stack.pop()

        for k in range(4):
            ny = V[0] + dy[k]
            nx = V[1] + dx[k]

            # 4방향 살펴서
            if 0 <= ny < N and 0 <= nx < N:
                # 도착점이면 1 리턴

                if miro[ny][nx] == 3:
                    return 1

                # 방문하지 않은곳이면 stack에 쌓아주고 방문표시
                elif miro[ny][nx] == 0 and visited[ny][nx] == 0:
                    stack.append([ny, nx])
                    visited[ny][nx] = 1
    # 다 탐색하고 안되면 0
    return 0
def dfs2(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []
    # 시작점 넣어주고
    stack.append([y, x])
    miro[y][x] = 1
    # 스택이 빌때까지
    while stack:

        V = stack.pop()

        for k in range(4):
            ny = V[0] + dy[k]
            nx = V[1] + dx[k]

            # 4방향 살펴서
            if 0 <= ny < N and 0 <= nx < N:
                # 도착점이면 1 리턴

                if miro[ny][nx] == 3:
                    return 1

                # 방문하지 않은곳이면 stack에 쌓아주고 방문표시
                elif miro[ny][nx] == 0:
                    stack.append([ny, nx])
                    miro[ny][nx] = 1
    # 다 탐색하고 안되면 0
    return 0

# def dfs_recursion(y, x):
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < N and 0 <= ny < N:
#             if miro[ny][nx] == 3:
#                 return 1
#             elif miro[ny][nx] == 0:
#                 miro[ny][nx] = 1
#                 dfs_recursion(ny, nx)
#     return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    miro = [ list(map(int, input())) for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            # 미로의 시작점에서 dfs 시작
            if miro[y][x] == 2:
                # print('#{} {}'.format(tc, dfs(y, x)))
                # print('#{} {}'.format(tc, dfs2(y, x)))
                print('#{} {}'.format(tc, dfs2(y, x)))

