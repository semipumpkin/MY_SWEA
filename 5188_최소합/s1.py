import sys
sys.stdin = open('input.txt', 'r')

def hab(y, x, total):
    global min_value
    if total > min_value:
        return

    if y == x == N - 1:
        if total <= min_value:
            min_value = total
        return
    # total += box[y][x]
    # visited[y][x] = 1
    # result += total
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny <= N - 1 and nx <= N - 1 and visited[ny][nx] == 0:

            visited[ny][nx] = 1
            hab(ny, nx, total + box[ny][nx])
            visited[ny][nx] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    box = [ list(map(int, input().split())) for _ in range(N) ]
    visited = [[0] * N for _ in range(N)]
    min_value = 99999999
    # first = box[0][0]
    dy = [0, 1]
    dx = [1, 0]
    # result = []
    hab(0, 0, box[0][0])
    print('#{} {}'.format(tc, min_value))
    # print(box)