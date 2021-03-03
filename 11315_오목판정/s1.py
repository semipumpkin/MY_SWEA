import sys
sys.stdin = open("input.txt", "r")


# 오목인 것을 확인하는 함수
def check(x, y):
    # 8개의 방향을 모두 확인
    for i in range(8):
        cnt = 1
        r, c = x + dx[i], y + dy[i]
        # 한 방향으로 계속 가는...
        while 0 <= r < N and 0 <= c < N and omok[r][c] == 'o':
            cnt += 1
            r, c = r + dx[i], c + dy[i]
            print(r,c)
        if cnt > 4: return True
    return False


# 중간 기준 올라가면 -1, 왼쪽 -1 (좌상은 무조건 -1)
# 상하좌우 우상우하좌하좌상
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

ans = ["NO", "YES"]

for tc in range(1, int(input()) + 1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]

    flag = 0
    # N * N이니까
    for i in range(N):
        for j in range(N):
            if omok[i][j] == '.': continue
            if check(i, j):
                flag = 1
                break
        if flag: break

    print("#{} {}".format(tc, ans[flag]))