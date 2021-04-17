import sys
sys.stdin = open('1.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    # print(N, M)
    # print(weights)
    total = 0
    trucks = sorted(trucks, reverse=True)
    weights = sorted(weights, reverse=True)
    # print(weights)
    # print(trucks)
    # 컨테이너의 무게를 돌면서
    visited = [0] * M
    for i in range(N):
        for j in range(M):
            if weights[i] <= trucks[j] and visited[j] == 0:
                visited[j] = 1
                total += weights[i]
                break
    print('#{} {}'.format(tc, total))

