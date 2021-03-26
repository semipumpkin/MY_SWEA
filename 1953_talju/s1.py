import sys
sys.stdin = open("input.txt", "r")

# 터널끼리 연결 = 탈주범 이동 가능.

# 탈주범이 있을 수 있는 위치의 개수

# 탈주범은 시간당 1

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    maps = [ list(map(int, input().split())) for _ in range(N) ]

    start = [R, C]

