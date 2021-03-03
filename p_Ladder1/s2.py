import sys
sys.stdin = open("input.txt", "r")

def find_boom(box):

    # 밑에서부터 찾아가자
    dx = [-1, 1, 0] # 좌우
    dy = [0, 0, -1] # 위방향
    start = 0
    for x in range(100):
        if box[99][x] == 2:
            start = x
    x = start
    y = 99
    while y > 0:

        # 방향을 살핀다 k는 방향. k가 0이면 좌 1이면 우 2면 위
        for k in range(3):
            nx = x + dx(k)
            ny = y + dy(k)



# x가 먹질 않느다.

for _ in range(10):
    tc = int(input())
    ladder = [ list(map(int, input().split())) for _ in range(100) ]
    # print(tc)
    print(find_boom(ladder))
