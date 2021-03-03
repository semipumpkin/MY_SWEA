import sys
sys.stdin = open("input.txt", "r")

def Quick_limited(nums):
    pass



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    print('#{}'.format(tc), *Quick_limited(num_list))