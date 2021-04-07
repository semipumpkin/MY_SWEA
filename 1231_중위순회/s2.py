import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    V = int(input())
    # temp = [[0, 0, 0, ''] for _ in range(V + 1)]
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(1, V+1):
        info = list(input().split())
