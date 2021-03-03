import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [ list(map(int, input().split())) for _ in range(N)]
    # print(rooms)
    stack = []
    room_list = [0] * 401
    # 쿠션 하나 넣기!
    for i in range(len(rooms)):
        room_list[rooms[i][0]] += 1
        room_list[rooms[i][1]] += 1
