import sys
sys.stdin = open("input.txt", "r")


def dump():
    # 최고 숫자와 최저 숫자 찾기
    # for i in range(10):
    n = int(input())
    nums = list(map(int, input().split()))
    max_n = min_n = nums[0]
    count = n
    # while count > 0:
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
                for l in range(len(nums)):
                    if nums[l] == min_n:
                        nums[l] += 1
                        count -= 1
    return nums

for i in range(10):
    print(dump())