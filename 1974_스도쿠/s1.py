import sys
sys.stdin = open("input.txt", "r")

# for문 , if문 + list로 나옴

T = int(input())
for tc in range(1, T+1):
    box = [list(map(int, input().split())) for _ in range(9)]

    num_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행 검사
    result = 1
    for y in range(9):
        # set으로 중복 제거 그리고 원소 비교
        if set(box[y]) != set(num_set):
            result = 0
            break

    # 열 검사
    for y in range(9):
        tmp = []
        for x in range(9):
            tmp.append(box[x][y])
        if set(tmp) != set(num_set):
            result = 0

    # 각 칸 검사
    # 0,0 / 0, 3 / 0, 6
    # 3, 0 / 3, 3 / 3, 6
    # 6, 0 / 6, 3 / 6, 6
    first = []
    for y in range(3):
        for x in range(3):
            total = []
            for i in range(3):
                for j in range(3):
                    total.append(box[3*y + i][3*x + j])
            if set(total) != set(num_set):
                result = 0
    print('#{} {}'.format(tc, result))