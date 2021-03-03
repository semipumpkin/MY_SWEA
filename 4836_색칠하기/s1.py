import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# matrix = [ [0]*10 for _ in range(10)]
T = int(input())
for tc in range(1, T + 1):
    # 새로운 행렬 초기화
    matrix = [[0] * 10 for _ in range(10)]
    N = int(input())

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 색깔이 칠해진 곳은 + 1
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                matrix[i][j] += 1

    # 색깔이 두번칠해진 곳은 보라색이므로 matrix에서 2인 곳만 count
    count = 0
    # for mat in matrix:
    #     count += mat.count(2)
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 2:
                count += 1
    print('#{} {}'.format(tc, count))
