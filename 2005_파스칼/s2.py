import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    pascal = [[1 for _ in range(i)] for i in range(1, N + 1)]
    for i in range(1, N):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    print('#{}'.format(tc))
    for i in range(N):
        print(*pascal[i])
