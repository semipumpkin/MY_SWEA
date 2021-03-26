import sys
sys.stdin = open("input.txt", "r")

def dfs(idx, total):
    # total = 0
    global min_value

    if total > min_value:
        return
    if idx == N and total < min_value:
        min_value = total

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx + 1, total + matrix[idx][i])
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    min_value = 10000000
    visited = [0] * N
    dfs(0,0)
    print('#{} {}'.format(tc, min_value))
            # 행에서 최솟값 그리고 열에서 최솟값


'''         
3 
2 1 2 / 1
5 8 5 / 5
7 2 2 / 2
3 
9 4 7 / 4
8 6 5 / 5
5 3 7 / 5
5
5 2 1 1 9 / 
3 3 8 3 1 / 
9 2 8 8 6 / 
1 5 7 8 3 /  
5 5 4 6 8 / 

#1 8
#2 14
#3 9
'''