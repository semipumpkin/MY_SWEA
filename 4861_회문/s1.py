import sys
sys.stdin = open("input.txt", "r")
#
#
T = int(input())



def again(N, M, box):
    # N * N 글자
    # M은 회문의 길이
    # 회문은 무조건 1개
    for y in range(N):
        #box의 각 행마다 살핌

        # x의 한 요소마다 M 길이의 회문이 되는지 안되는지 살펴봄
        for x in range(N - M + 1):


            # 가로 회문 판별
            # M을 2로 나눈 몫만큼만 뒤에 요소가 같은지 확인하면 회문 판별 가능
            # M 길이의 단어에서 회문 판별
            for i in range(M // 2):
                # 맨 첫번째 글자와 맨뒷글자 비교 -> 두번째 글자와 뒤에서 두번째 글자 비교 ->
                if box[y][x + i] != box[y][x + M - i -1]:
                    break
                else:
                    return






for tc in range(1, T+1):
    n, m = map(int, input().split())
    string_list = [ input() for _ in range(n) ]
#     # print(string_list)
    print('#{} {}'.format(tc, again(n, m, string_list)))









def recur_string(N, M, str_list):
    # 회문은 최소 글자 5개
    # N * N 길이 M 회문
    # 회문은 무조건 1개
    # 1개만 찾으면 break
    # 5 <= M <= N

    # 세로인 문자열을 str_list에 추가함
    for y in range(N):
        sero = ''
        for x in range(N):
            sero += str_list[x][y]
        str_list.append(sero)

    # 가로문자만 회문확인해서 찾으면 됨
    for y in range(2*N):

        # 각 행마다 확인
        for x in range(N - M+1): # 각 원소마다 M의 길이만큼 슬라이싱

            # M의 개수만큼 슬라이싱
            compare = str_list[y][x : x + M + 1]


            count = 0
            # 슬라이싱된 문자열에서 M // 2의 개수만큼 앞뒤 문자를 하나씩 비교하여 같다면 count를 늘려줌
            for i in range(len(compare) // 2):
                if compare[i] == compare[len(compare) -1 - i]:
                    count += 1

            # count가 M//2이면 return
            if count == len(compare) // 2:
                return compare
