import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    numsi = list(map(int, input().split()))
    c_list = list(map(int, input().split()))


    K = numsi[0]
    N = numsi[1]
    M = numsi[2]
    # gan은 N을 충전기 개수로 나눈 수
    # 만약 정류장의 수를 K로 나눈다면 최소 필요한 충전기의 개수가 나오는데 이 수가 충전기의 개수보다 적다면 버스는 절대 종점에 도착불가능하다.
    # 최소 필요한 충전기의 개수를 N // K로 지정하고,
    if N // K < M:
        mini = N // K
        for j in range(len(c_list) - 1):
            # 각 충전기 사이의 거리가 버스가 한번 충전에 갈 수 있는 거리K 보다 크다면 버스는 종점에 도착 불가능
            if c_list[j + 1] - c_list[j] > K:
                mini = 0
    elif N // K == M:
        if  N % K == 0:
            for k in range(len(c_list) - 1):
                if c_list[k + 1] - c_list[k] == K:
                    mini = N // K - 1
                else:
                    mini = 0
        else:
            mini = N // K

    else:
        mini = 0
    print('#{} {}'.format(i, mini))


