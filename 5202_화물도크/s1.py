import sys
sys.stdin = open('1.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    infos = [ list(map(int, input().split())) for _ in range(N)]
    print(infos)

    infos.sort(reverse=True)
    print(infos)
    result = 1
    start = infos[0][0]
    for i in range(1, N):
        if infos[i][1] <= start:
            result += 1
            start = infos[i][0]
    print('#{} {}'.format(tc, result))
