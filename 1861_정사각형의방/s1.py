import sys
sys.stdin = open('1.txt', 'r')

#
def bfs(y, x, count, val):
    global max_value

    # for y in range(N):
    #     for x in range(N):
    # visited[y][x] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if box[ny][nx] == box[y][x] + 1:
                # visited[nx][ny] = 1
                bfs(ny, nx, count + 1, val)
                # visited[nx][ny] = 0
    if count and count >= max_value:
        max_value = count
        result.append((val, max_value + 1))


for tc in range(1, int(input()) + 1):
    # for tc in range(1, 3):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    # print(box)
    result = []
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    max_value = -999999
    for i in range(N):
        for j in range(N):
            # visited = [[0] * N for _ in range(N)]
            bfs(i, j, 0, box[i][j])
    result.sort(key=lambda x: (-x[1], x[0]))
    # print(result)
    # result.sort()
    print('#{} {} {}'.format(tc, result[0][0], result[0][1]))
    # print('#{}'.format(tc), *result[0])