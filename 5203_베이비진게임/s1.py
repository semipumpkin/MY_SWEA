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
        while cnt_list[i] and cnt_list[i+1] and cnt_list[i+2]:
            count += 1
            cnt_list[i] -= 1
            cnt_list[i+1] -= 1
            cnt_list[i+2] -= 1

    return count
T = int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    player1 = []
    player2 = []
    winner = 0
    for i in range(len(temp)):
        if i % 2 == 0:
            player1.append(temp[i])

            if is_babygin(player1):
                winner = 1
                break
        else:
            player2.append(temp[i])
            if is_babygin(player2):
                winner = 2
                break
    print('#{} {}'.format(tc, winner))
    # print(is_babygin(player2))