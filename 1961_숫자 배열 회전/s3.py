import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 행렬의 수
    arr = [[[0] * N for _ in range(N)] for _ in range(4)]
    for i in range(N):
        arr[0][i] = list(map(int, input().split()))

    # 회전
    for k in range(1, 4):
        for i in range(N):
            for j in range(N):
                arr[k][j][N - 1 - i] = arr[k - 1][i][j]

    # 출력
    print("#{}".format(tc))
    for i in range(N):
        for k in range(1, 4):
            if k != 1: print(end=" ")
            for j in range(N):
                print(arr[k][i][j], end="")
        print()
