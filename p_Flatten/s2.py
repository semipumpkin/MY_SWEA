import sys
sys.stdin = open("input.txt", "r")

def dump(n, nums):
    # 최고 숫자와 최저 숫자 찾기
    count = n
    while count > 0:
        max_n = min_n = nums[0]
        for i in range(len(nums)):
            if max_n <= nums[i]:
                max_n = nums[i]
        for j in range(len(nums)):
            if min_n >= nums[j]:
                min_n = nums[j]
                # 최고 숫자에서 -1 최저 숫자에서 + 1
        for k in range(len(nums)):
            if nums[k] == max_n:
                nums[k] -= 1
                break
        for l in range(len(nums)):
            if nums[l] == min_n:
                nums[l] += 1
                break
        count -= 1
    max_n = min_n = nums[0]
    for i in range(len(nums)):
        if max_n <= nums[i]:
            max_n = nums[i]
    for j in range(len(nums)):
        if min_n >= nums[j]:
            min_n = nums[j]
    return max_n - min_n
for i in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    print('#{} {}'.format(i, dump(N, height)))