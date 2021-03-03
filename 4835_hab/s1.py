import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = (map(int, input().split()))
    nums = list(map(int, input().split()))
    # print(N, M, nums)
    # N은 정수의 개수
    # M은 구간의 개수
    totals = []
    # i부터 i + M 까지
    for i in range(len(nums) - M + 1):
        totals += [sum(nums[i: i + M ])]
    max_value = min_value = totals[0]
    for j in range(len(totals)):
        if max_value <= totals[j]:
            max_value = totals[j]
    for k in range(len(totals)):
        if min_value >= totals[k]:
            min_value = totals[k]
    print('#{} {}'.format(tc, max_value - min_value))



