import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(N) ]
    # matrix = [ list(map(int, input().split())) for _ in range(N) ]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    total = 0
    #
    # for i in range(1, N - 1):
    #     for j in range(1, N - 1):
    #         abs_sum = 0
    #         for k in range(4):
    #             center = matrix[i][j]
    #             nx = i + dx[k]
    #             ny = j + dy[k]
    #             abs_sum += abs(matrix[nx][ny] - center)
    #         total += abs_sum
    # print(total)
    for i in range(N):
        for j in range(N):
            abs_sum = 0
            for k in range(4):
                center = matrix[i][j]
                nx = i + dx[k]
                ny = j + dy[k]
                if N > nx >= 0 and N > ny >= 0:
                    abs_sum += abs(matrix[nx][ny] - center)
            total += abs_sum
    print(total)
