import sys
sys.stdin = open("input.txt", "r")

def hamburger(idx):
    global max_satisfaction
    if idx == N:
        # print(visited)
        kcal = 0
        satisfaction = 0
        for i in range(N):
            kcal += ingredients[i][1] * visited[i]
            satisfaction += ingredients[i][0] * visited[i]
        if kcal > L:
            return
        if satisfaction > max_satisfaction:
            max_satisfaction = satisfaction

        return
    visited[idx] = 1
    hamburger(idx+1)
    visited[idx] = 0
    hamburger(idx+1)


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    # max_kcal = L
    ingredients = [ list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # hamburger(0)
    max_satisfaction = 0
    # print(max_satisfaction)
    # print(visited)
    hamburger(0)
    print('#{} {}'.format(tc, max_satisfaction))