import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in (1, T + 1):
    N = int(input())

    # 빈 2차원 배열 만들기
    box = [[0]*N for _ in range(N)]

         #우 하 좌 상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    idx = 0
    n = 0
    x = -1
    y = 0

    # 방향 델타를 for문 조건으로 걸어서 풀어보기
    while n < N * N:
        nx = x + dx[idx]
        ny = y + dy[idx]

        # 계속 0이 숫자로 바뀔 예정


        if not (0 <= ny < N and 0 <= nx < N) or box[ny][nx] != 0:
            if idx == 3:
                idx = 0
            else:
                idx += 1

        else:
            n += 1
            box[ny][nx] = n
            x, y = nx, ny
    print('# {}'.format(tc))
    for line in box:
        print(' '.join(map(str, line)))



    # 방향 전환









