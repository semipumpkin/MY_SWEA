import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    words = [ input()for _ in range(5)]
    # length_list = []

    # 각 문자열의 최대길이 찾음
    length_max = 0
    for i in range(len(words)):
        if len(words[i]) > length_max:
            length_max = len(words[i])


    # 빈공간에 .을 채워넣음
    for i in range(len(words)):
        while len(words[i]) < length_max:
            words[i] += '.'

    # 세로로 뽑아서 일렬로 더해줌
    sero = ''
    for y in range(length_max):
        for x in range(len(words)):
            sero += words[x][y]

    # . 제거
    answer = sero.replace('.', '')
    print('#{} {}'.format(tc, answer))

