import sys
sys.stdin = open("input.txt", "r")

# 유망성 체크
def promising(box, y, x):
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        # 탐색 종료조건
        while 0 <= nx < N and 0 <= ny < N:
            # 8가지 방향에서 퀸을 만나지 않는다면 계속 쭉 감
            if box[ny][nx] == 0:
                nx = nx + dx[k]
                ny = ny + dy[k]

            # 퀸을 만난다면 0반환
            else:
                return False
    # 위 과정을 다 거쳤다면 y,x 기준으로 다른 queen이 없는 것이므로 True 반환
    return True

def queens(idx, box):

    global ans
    # 모든 행을 다 돌았을때, queen이 서로 공격할 수 없으므로
    if idx == N:
        ans += 1

    # idx행의 열들을 탐색
    for i in range(N):

        # 유망성 검사
        if promising(box, idx, i):

            # 유망하다면 방문체크
            box[idx][i] = 1
            queens(idx + 1, box)
            box[idx][i] = 0
        # 유망하지 않다면 함수 종료





dy = [1, -1, 0, 0, 1, -1, 1, -1]
dx = [0, 0, 1, -1, -1, -1, 1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    queen = [[0] * N for _ in range(N)]
    ans = 0


    queens(0, queen)
    print('#{} {}'.format(tc, ans))