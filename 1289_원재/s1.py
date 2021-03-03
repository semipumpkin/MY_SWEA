import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 01010101010101010101010101010101010101010101010101
    # 00000000000000000000000000000000000000000000000000

    # 원본
    original = input()

    # 초기화 리스트
    reset = ['0']*len(original)

    count = 0
    if original[0] == '1':  # 1일때는 1로 모두 채움
        count += 1
        reset = [1] * len(original)
    for i in range(len(original) - 1):

        # 원본과 reset이 같지 않다면 뒤에 모든 요소 1로 바꿔줌
        if original[i] != reset and original[i] == '1' and original[i] != original[i+1]:
            # 그 뒤의 모든 요소를 바꿔줌
            for j in range(i, len(original)):
                reset[j] = '1'
            count += 1
        # 원본과 reset이 같지 않다면 뒤에 모든 요소 0으로 바꿔줌
        elif original[i] != reset and original[i] == '0' and original[i] != original[i+1]:
            # 그 뒤의 모든 요소를 바꿔줌
            for j in range(i, len(original)):
                reset[j] = '0'
            count += 1

        # 앞뒤가 같을 경우 스킵
        else:
            continue
    print('#{} {}'.format(tc, count))