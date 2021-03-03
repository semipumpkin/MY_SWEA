import sys
sys.stdin = open("input.txt", "r")

T = int(input())
nums = list(range(1, 13))

for tc in range(1, T + 1):
    # print(tc)
    N, K = map(int, input().split())
    # 부분집합의 개수가 N 합이 K이면 count
    count = 0

    for i in range(1<<12):
        # print(i)
        num_sum = 0
        cnt = 0
        for j in range(12):
            if i & (1<<j):
                num_sum += nums[j]
                cnt += 1
        # 부분집합의 개수가 N, 합이 K이면 count를 더해줌
        if cnt == N and num_sum == K:
            count += 1
    print('#{} {}'.format(tc, count))
