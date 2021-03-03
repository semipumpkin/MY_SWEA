import sys
sys.stdin = open("input.txt", "r")
# from Pandas import Dataframe

V, T = map(int, input().split())

temp = [ [0]*(V + 1) for _ in range(V+1) ]

visited = [0] * (V + 1)

nums = list(map(int, input().split()))

for i in range(len(nums)//2):
    temp[nums[i*2]][nums[i*2 + 1]] = 1
    temp[nums[i*2 + 1]][nums[i*2]] = 1

def dfs(v):
    # 방문한 곳.
    stack = []

    # 정점 방문
    stack.append(v)

    # stack이 비어있을때 까지 반복
    while len(stack):
        # 가장 최근에 방문한 정점을 pop
        print(stack)
        y = stack.pop()

        # 만약 방문하지 않았다면
        if visited[y] == 0:

            # 방문처리
            visited[y] = 1
            print(y, end='을 방문 했습니다.')
        print()

        # 그리고 y와 연결된 노드들을 검색
        for x in range(1, V + 1):

            # 노드가 연결되있고, 그 연결된 노드가 방문되지 않았다면
            if temp[y][x] == 1 and visited[x] == 0:

                # stack에 그 노드를 넣어줌
                # 길이 막히면 정점으로 돌아가기 위해
                stack.append(x)
def recur_dfs(v):
    visited[v] == 1
    print(v, end= ' ')
    for i in range(1, V+1):
        if temp[v][i] == 1 and visited[i] == 0:
            recur_dfs(i)
print(dfs(3))

