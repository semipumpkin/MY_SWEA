import sys
sys.stdin = open('input.txt')

























    #
    #
    #
    # N = int(input())
    # matrix = [list(map(int, input())) for i in range(N)]
    # result = 0
    #
    # # N이 1인 경우 result는 matrix 값 그대로
    # if N == 1:
    #     result = matrix[0][0]
    # else:
    #     # 열이 하나씩 늘어날 때 마다 중간 행을 기준으로 좌우 하나씩 범위가 늘어남
    #     # 열이 중간을 넘어가면 좌우 하나씩 범위가 줄어듬
    #     k = 0  # 인덱스 접근
    #     for i in range(N):
    #         for j in range(N // 2 - k, N // 2 + 1 + k):
    #             result += matrix[i][j]  # 결과 더해줌
    #         # 알고리즘 조건
    #         if i < (N // 2):
    #             k += 1
    #         else:
    #             k -= 1
    # print('#{} {}'.format(test, result)