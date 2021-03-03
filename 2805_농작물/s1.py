import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    box = [list(map(int, input())) for _ in range(N)]
    answer = 0

    # 차라리 끝에 원소들을 다 0으로 만들어주고 각줄마다 더해버리자

    # 1
    ans = 0
    for y in range(N//2):
        for x in range(N//2 - y):
            box[y][x] = 0
            box[y][N-x - 1] = 0
            box[N-x-1][y] = 0
            box[N-x-1][N-y-1] = 0
    for i in range(N):
        ans += sum(box[i])
    print('#{} {}'.format(tc, ans))


    # box[y][N//2 + 1]
    # box[y][N//2] + box[y][N//2 + 1] + box[y][N//2 + 2]
    # box[y][N//2 - 1] +  box[y][N//2] + box[y][N//2 + 1] + box[y][N//2 + 2] + box[y][N//2 + 3]

