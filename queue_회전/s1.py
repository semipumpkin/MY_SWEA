import sys
sys.stdin = open("input.txt", "r")

# def bfs(items):


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    i = 0
    while i < M:
        T = nums.pop(0)
        nums.append(T)
        i += 1
    print('#{} {}'.format(tc, nums[0]))