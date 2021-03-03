import sys
sys.stdin = open("input.txt", "r")

def Quick(nums):


    # 종료 조건
    if len(nums) <= 1:
        return nums

    left = []
    right = []
    pivot = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > pivot:
            right.append(nums[i])
        else:
            left.append(nums[i])
    return [*Quick(left), pivot, *Quick(right)]



T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    # print(*num_list)
    print(Quick(num_list))