import sys
sys.stdin = open('1.txt', 'r')

def visit(y, next, total):
    global min_value
    if total > min_value:
        return
    if y == N-1:
        total += box[next][0]
        if total <= min_value:
            min_value = total
            return

    for x in range(N):
        if visited[x] == 0 and box[next][x]:


            visited[x] = 1
            visit(y+1, x, total + box[next][x])
            visited[x] = 0



for tc in range(1, int(input())+1):
    N = int(input())
    box = [ list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_value = 99999999
    visited[0] = 1
    visit(0, 0, 0)
    print('#{} {}'.format(tc, min_value))