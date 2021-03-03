import sys
sys.stdin = open("input.txt", "r")
    # print(pan)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# 서 북서 북 북동 동 남동 남 남서

def is_omok(n, box):
    for y in range(n):
        for x in range(n):
            # 돌이 있을때,
            if box[y][x] == 'o':

                # 각 방향을 탐색해서 그 방향에 돌이 있다면 그 방향으로 쭉 탐색
                for k in range(8):
                    count = 1
                    nx = x + dx[k]
                    ny = y + dy[k]
                    while 0 <= nx < n and 0 <= ny < n and box[ny][nx] == 'o':
                        count += 1
                        ny, nx = ny + dy[k], nx + dx[k]
                    if count > 4:
                        return True
    return False


                # 그 방향에 돌이 5개이상이면 YES 리턴

                # 전체를 다 돌았는데도 5개이상으로 연속인 돌이 없다면 NO 리턴





T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pan = [ input() for _ in range(N)]
    ans = ['NO', 'YES']
    print('#{} {}'.format(tc, ans[is_omok(N, pan)]))