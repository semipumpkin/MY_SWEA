import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price_list = list(map(int, input().split()))
    result = 0

    idx = 0
    max_idx = 0
    # 처음부터 max까지의 인덱스를 찾고
    # max 인덱스 전까지 모든 원소를 max값과 빼서 result에 더해줌
    # 그리고 인덱스를 다시 max_idx로 초기화하고 다시 그 뒤에 max를 찾아서 빼줌

    while idx < N:

        # idx부터 N까지 가장 큰 수의 인덱스를 찾는다
        for i in range(idx, N):
            if price_list[max_idx] < price_list[i]:
                max_idx = i
        # 가장 큰수를 찾고 그 날에 판다.
        for j in range(idx, max_idx):
            result += price_list[max_idx] - price_list[j]
        # 팔고 나서 그 다음날부터 새로 시작하기 위해
        # 시작인덱스를 정해준다.
        max_idx += 1
        idx = max_idx
    print(result)

