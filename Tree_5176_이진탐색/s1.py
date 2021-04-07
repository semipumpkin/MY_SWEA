import sys
sys.stdin = open('input.txt', 'r')

def awef(node):
    global num
    if 0 < node <= N:
        awef(node*2)
        temp[node] = num
        num += 1
        awef(node*2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = [0] * (N + 1)
    num = 1
    awef(1)
    print('#{} {} {}'.format(tc, temp[1], temp[N//2]))