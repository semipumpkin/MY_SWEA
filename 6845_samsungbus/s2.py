import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # bus_stop의 개수가 왜 5001개지?
    # 왜냐하면 첫번째 요소를 비워놓기 때문!
    bus_stop = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            bus_stop[j] += 1


    # 총 버스 정류장의 개수
    P = int(input())
    # bus_stop_cnt = bus_stop[1 : P + 1]
    # 왜 이렇게 슬라이싱 하면 안되는지 잘 이해가 안간다.
    # print('#{}'.format(tc), end=" ")
    # for k in range(len(bus_stop_cnt):
    #     C = int(input())
    #     print(bus_stop_cnt[C], end=" ")
    # print()

    print('#{}'.format(tc), end=" ")
    for k in range(P):
        C = int(input())
        print(bus_stop[C], end=" ")
    print()