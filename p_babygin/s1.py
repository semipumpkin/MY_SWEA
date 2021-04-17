import sys
sys.stdin = open("input.txt", "r")

    # tri 같은숫자가 3개 연속
    # run 숫자의 연속 3개
    # babygin이란 연속한 숫자이거나 같은숫자가 3개 인 숫자들이 2개 이상이면 true
def is_babygin(nums):
    cnt_list = [0] * 10 # 숫자의 범위가 0~9까지
    for i in range(len(nums)):
        cnt_list[nums[i]] += 1
    count = 0
    # tri pallet
    for i in range(len(cnt_list)):
        while cnt_list[i] >= 3:
            count += 1
            cnt_list[i] -= 3

    # run 판별
    for i in range(len(cnt_list) - 2):
        while cnt_list[i] and cnt_list[i+1] and cnt_list[i+2] > 0:
            count += 1
            cnt_list[i] -= 1
            cnt_list[i+1] -= 1
            cnt_list[i+2] -= 1

    return count

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input()))
    # print(nums)
    print(is_babygin(nums))


























# T = int(input())
# for tc in range(1, T+1):
#     nums = list(map(int, input()))
#     nums_count = [ 0 for _ in range(10)]
#     tri = run = 0
#     for num in nums:
#         nums_count[num] += 1
#         for n in nums_count:
#             if n >= 3:
#                 tri += 1
#                 nums_count[num] = 0
#         for i in range(len(nums_count) - 2):
#             while nums_count[i] > 0:
#                 if nums_count[i] and nums_count[i + 1] and
#                 run += 1
#                 nums_count[i] -= 1
#                 nums_count[i + 1] -= 1
#                 nums_count[i + 2] -= 1

    # print(run, tri)
    #
