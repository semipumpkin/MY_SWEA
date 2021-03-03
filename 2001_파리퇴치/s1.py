import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [ list(map(int, input().split())) for _ in range(N)]

    # 파리 최대값
    max_num = 0
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            # 한번 후릴때마다 잡는 파리의 수
            fly = 0
            for i in range(M):
                for j in range(M):
                    fly += matrix[y + i][x + j]

            # 파리 최대값 찾기
            if max_num < fly:
                max_num = fly
    print('#{} {}'.format(tc, max_num))