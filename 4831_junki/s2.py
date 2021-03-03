import sys
sys.stdin = open("input.txt", "r")

# T = int(input())

    # K 는 한번 충전에 갈 수 있는 거리
    # N은 정류장의 종점
    # M은 충전기가 설치된 개수

    # 출발지에서 충전되잇는 상태로 시작

    # 현재 위치 설정 for 문의 i, 현재에서 갈 수있는 거리 togo 설정
def Bus(K, N, M, bus_stop):
    location = K
    charge = 0
    last_charge = 0
    while location < N:
        if last_charge == location:
            return 0
        if bus_stop[location]:
            charge += 1
            last_charge = location
            location += K
        else:
            location -= 1
        # print(location)
    return charge

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_stop = [0] * (N+1)
    for i in list(map(int, input().split())):
        bus_stop[i] = 1
    print('#{} {}'.format(tc, Bus(K, N, M, bus_stop)))