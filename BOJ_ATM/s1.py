
N = int(input())
P = list(map(int, input().split()))
# P = [3, 1, 4, 3, 2]
P.sort()

total = 0
T = len(P)
for i in range(1, T+1):
    total += (T-i+1)*P[i - 1]
print(total)