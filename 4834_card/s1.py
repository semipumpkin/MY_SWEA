import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for i in range(1, T + 1):
    ni = int(input())
    nums = list(map(int, input()))
    cnt = [ 0 for _ in (range(10))]
    for number in nums:
        cnt[number] += 1
    max_cnt = cnt[0]
    for j in range(len(cnt)):
        if max_cnt <= cnt[j]:
            max_cnt = cnt[j]
            max_number = j
    print('#{} {} {}'.format(i, max_number, max_cnt))