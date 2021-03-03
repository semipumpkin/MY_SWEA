import sys
sys.stdin = open("input.txt", "r")

# N = input()
N = int(input())
# print(N)
# print(type(N))
if N % 2:
    result = 1
else:
    result = 0
print(N)

# nums = input()
# print(type(nums)) 이 친구는 문자열!
# 공백이 있는 문자열을 공백을 기준으로 잘라서

# 문자열 요소를 가진 리스트로 만들겠다!
# nums = input().split()

nums = list(map(int, input().split()))

total = 0
for num in nums:
    total += num
print(total)

N = int(input())
rl = []
for _ in range(N):
    rl.append(list(map(int, input().split())))
print(rl[1][1])