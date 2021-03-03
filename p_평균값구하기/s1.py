import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    result = round(sum(nums) / len(nums))
    print("#{} {}".format(tc, result))
