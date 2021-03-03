import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 시간 = 거리/속력
    time = D / (A+B)
    print('#{} {}'.format(tc, time*F))
'''
250
10 20
15 235
20 

'''
