import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrival = list(map(int, input().split()))
    # M초의 시간을 들여 K개의 붕어빵을 만들수있음
    # 붕어빵의 개수
    '''
    
    '''
    total = 0
    i = 0
    bbang = 0
    sec = 0
    while i < N:

        bbang += K
        sec += M
        total += arrival[i]
        if total < sec:
            print('Impossible')
            break
        else:
            bbang -= 1
            i += 1
            # total += arrival[i]



