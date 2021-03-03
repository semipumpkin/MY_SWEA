import sys
sys.stdin = open("input.txt", "r")

# 사다리 그리기 ( 0인 행렬에 사다리가 지나가는 곳 + 1)
for _ in range(10):
    tc = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(100) ]
#     # print(matrix)
    # 시작점 인덱스 찾아놓기
    x_list = []
    for i in range(100):
        if matrix[0][i] == 1:
            x_list += [i]

    boom = 0
    for k in x_list:
        x = k
        y = 0
        while matrix[x][y] != 2:
            # 계속 더해줌

            # 방향이 좌일때 아래 수가 1일때까지 계속 -1을 반복해준다.
            if 0 <= x - 1 and matrix[y][x - 1] == 1:
                x -= 1
                while matrix[y + 1][x] != 1:
                    x -= 1
                y += 1
            # 방향이 우일때 아래 수가 1일때까지 계속 +1을 반복해준다
            elif x < 99 and matrix[y][x + 1] == 1:
                x += 1
                while matrix[y + 1][x] != 1:
                    x += 1
                y += 1
            # 방향이 아래일때 y를 1 더해줌
            elif y < 99 and matrix[y + 1][x] == 1:
                y += 1

            # 쭉 더해주다가 2인 원소를 만나면 멈춰줌
            elif y < 99 and matrix[y + 1][x] == 2:
                y += 1
                break
            # print(x)
            # 나머지 경우에는 반복문을 멈춰줌
            else:
                break

        # 2에 도착했을때 시작점의 x 좌표 k를 저장
        if matrix[y][x] == 2:
            boom += k
            break
    print('#{} {}'.format(tc, boom))





























# 첫번째 행렬을 돌며 1인 곳 찾기

# 1인 곳을 찾는다면 밑으로 내려감

# 밑으로 내려가면서 좌우에 1이 있다면 방향을 좌우로 바꿈

# 좌우로 바꾸다가 아래로 1이 있다면 방향을 아래로 바꿈

# 그렇게 끝까지 진행하고 만약 마지막 열의 값이 2이면 시작 지점의 좌표를 도출






