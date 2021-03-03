import sys
sys.stdin = open("input.txt", "r")
#
def is_palindrom(matrix):
    # M이 나올 수 있는 가장 큰 수부터 아래로 가면서 나오면 그냥 끝내자.
    for M in range(100, -1, -1):

        palindrom = ''


        # 가로
        for i in range(len(matrix)):

            for j in range(len(matrix) - M + 1):


                for k in range(M // 2):
                    if matrix[i][j + k] != matrix[i][j + M - 1 - k]:
                        break
                else:
                    for l in range(j, j + M):
                        palindrom += matrix[i][l]

        for i in range(len(matrix)):

            for j in range(len(matrix) - M + 1):

                # 세로
                for k in range(M // 2):
                    if matrix[j + k][i] != matrix[j + M - 1 - k][i]:
                        break

                else:
                    for l in range(j, j + M):
                        palindrom += matrix[i][l]

        if palindrom:
            return M



# tc는 총 10개임
for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(str, input())) for _ in range(100)]

    print('#{} {}'.format(N, is_palindrom(matrix)))