import sys
sys.stdin = open('input.txt', 'r')



'''
123 - > 3 2 1
2737 -> 7732
32888 -> 88832
456789 -> 
956784
986754
987654
987645
987654
987645
987654
987645
987654
987645

'''

def swapping(cnt):
    if cnt == n:

        return



T = int(input())
for tc in range(1, T+1):
    cards, n = input().split()
    nums = list(map(int, cards))
    # print(nums)
    cnt = 0
    visited = [0] * len(nums)
    print(swapping(cnt))

    # print(nums[0:])