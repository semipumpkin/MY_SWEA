import sys
sys.stdin = open('input.txt')

# 각 배열에서 A, B, C를 찾는다
# 방향델타 상하좌우 설정
# A를 찾으면w 방향델타를 한번만 탐색. 탐색 후 O로 바꿔줌
# B를 찾으면 2번, C를 찾으면 3번
# 위 과정을 해주고 H인 요소를 카운트해서 반환해주면 끝

def check(x, y):
    # 4방향 올리기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스 체크, H일때 X로 바꾸기
        for j in range(ord(arr[x][y]) - ord('A') + 1):  # A B C에 따라 다르게
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                arr[nx][ny] = 'X'
                nx = nx + dx[i]
                ny = ny + dy[i]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 0

    # 출력하기
    # for i in arr:
    #     print(*i)
    # print()

    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            # if arr[i][j] != 'X' and arr[i][j] != 'H':
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                check(i, j)
    # H 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                ans += 1
    # 출력하기
    # for i in arr:
    #     print(*i)

    print("#{} {}".format(tc, ans))