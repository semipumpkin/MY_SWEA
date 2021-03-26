import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    min_count = 1000000
    flag = [list(input()) for _ in range(N)]

    cnt = 0
    for y in range(0, N-2):
        for x in range(M):
            if flag[y][x] != 'W':
                cnt += 1
        cnt2 = 0
        for y1 in range(y+1, N-1):
            for x1 in range(M):
                if flag[y][x1] != 'B':
                    cnt2 += 1
            cnt3 = 0
            for y2 in range(y1+1, N):
                for x2 in range(M):
                    if flag[y2][x2] != 'R':
                        cnt3 += 1
            cnt += cnt2 + cnt3
            if min_count > cnt:
                min_count = cnt
    print(min_count)

'''
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW W - 8
WRRRWWWBWWWWRB W - 6
WWBWBWWWBWRRRR W - 7
WBWBBWWWBBWRRW B - 9
WWWWWWWWWWWWWW R - 14

각 행을 탐색하면서 싹다 해보자
[W, B, R] W+B+R = N
while W > 2:

'''