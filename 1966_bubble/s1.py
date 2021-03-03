import sys
sys.stdin = open("input.txt", "r")

def bubble(nums):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums
def bubble_reverse(nums):
    for i in range(len(nums)-1, 0,-1):
        for j in range(i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
def bubble_reverse2(nums):
    for i in range(len(nums) -1, -1, -1):
        for j in range(i):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # print(bubble(num_list))
    #
    # print(bubble_reverse(num_list))
    print(bubble_reverse2(num_list))