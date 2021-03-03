import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))

    # 두개의 리스트를 나눠줌.
    first = []
    second = []
    for i in range((N + 1) // 2):
        first.append(cards[i])
    for i in range(N // 2):
        second.append(cards[N -(N // 2) + i])

    # 각 리스트에서 하나씩 뽑아서 result에 넣어줌
    result = []
    for i in range(len(second)):
        result.append(first[i])
        result.append(second[i])

    # 만약 first 리스트가 더 크다면 result의 마지막에 넣어줘서 완성 시킴.
    if len(first) > len(second):
        result.append(first[-1])
    print('#{}'.format(tc), *result)

