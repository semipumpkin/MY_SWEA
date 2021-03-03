import sys
sys.stdin = open("input.txt", "r")

dy = [-1, 1, 0 ,0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]
    # 상 하 좌 우 북서 북동 남동 남서
def check_black(y, x):
    # 방향 탐색
    # stack = []
    for k in range(8):
        ny = y + dy[k]
        nx = x + dx[k]

        # 범위 설정, 그리고 그 방향에 백돌이 있다면 그 방향으로 한칸 더 탐색해서

        while 1 <= nx < N+1 and 1<= ny < N + 1:
            if pan[ny][nx] == 0:
                break
            elif pan[ny][nx] == 1:
                while ny != y or nx != x:
                    ny -= dy[k]
                    nx -= dx[k]
                    pan[ny][nx] = 1
                break
            ny += dy[k]
            nx += dx[k]

def check_white(y, x):
    # stack = []
    for k in range(8):
        ny = y + dy[k]
        nx = x + dx[k]
        while 1 <= nx < N+1 and 1<= ny < N + 1:
            if pan[ny][nx] == 0:
                break
            elif pan[ny][nx] == 2:
                while ny != y or nx != x:
                    ny -= dy[k]
                    nx -= dx[k]
                    pan[ny][nx] = 2
                break
            ny += dy[k]
            nx += dx[k]

# def check_black(y, x):
#     # 방향 탐색
#     stack = []
#     for k in range(8):
#         ny = y + dy[k]
#         nx = x + dx[k]
#
#         # 범위 설정, 그리고 그 방향에 백돌이 있다면 그 방향으로 한칸 더 탐색해서
#
#         if 1 <= nx < N+1 and 1<= ny < N + 1 and pan[ny][nx] == 2:
#             nx += dx[k]
#             ny += dy[k]
#
#             if 1 <= nx < N+1 and 1<= ny < N + 1 and pan[ny][nx] == 1:
#                 pan[ny - dy[k]][nx - dx[k]] = 1
#
#
# def check_white(y, x):
#     stack = []
#     for k in range(8):
#         ny = y + dy[k]
#         nx = x + dx[k]
#         if 1 <= nx < N+1 and 1<= ny < N + 1 and pan[ny][nx] == 1:
#             nx += dx[k]
#             ny += dy[k]
#             if 1 <= nx < N+1 and 1<= ny < N + 1 and pan[ny][nx] == 2:
#                 pan[ny - dy[k]][nx - dx[k]] = 2





T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    dols = [list(map(int, input().split())) for _ in range(M)]
    pan = [ [0]*(N + 1)  for _ in range(N + 1)]

    # 초기 설정
    for y in range(2):
        for x in range(2):
            pan[N//2 + y][N//2 + x] = 1
    pan[N//2 + 1][N//2 + 1] = 2
    pan[N//2][N//2] = 2

    # 돌을 놓아주면서 흑일때와 백일때를 구분
    # 돌을 놓았을 때, 그 돌 주변을 확인
    flag = 1
    for dol in dols:

        # 흑일때
        if dol[2] == 1:
            # 돌을 놓고
            pan[dol[1]][dol[0]] = 1
            check_black(dol[1], dol[0])
            # flag = 1
        # 백일때
        elif dol[2] == 2:
            pan[dol[1]][dol[0]] = 2
            check_white(dol[1], dol[0])
            # flag = 2
    count1 = 0
    count2 = 0
    for y in range(len(pan)):
        count1 += pan[y].count(1)
        count2 += pan[y].count(2)
    print('#{} {} {}'.format(tc, count1, count2))