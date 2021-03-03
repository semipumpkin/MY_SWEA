import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    price_list = list(map(int, input().split()))
    max_idx = 0
    idx = 0
    while idx < N:
        # 각 요소를 돌아가면서 뽑아주며
        for i in range(idx, len(price_list)):
            if price_list[idx] > price_list[max_idx]:
                max_idx = idx
        # 그 뒤의 최대값을 찾음


        # 최대값 전에 있는 모든 요소들과 최댓값의 차이를 result에 더해줌


        # 최댓값 인덱스를 idx로 초기화
        # 그리고 위 과정 반복

