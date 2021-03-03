import sys
sys.stdin = open('input.txt')

# 출발점은 0 도착점은 99

# 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.

# 단 화살표 방향을 거슬러 돌아갈 수는 없다.


for _ in range(1, 11):
    tc, N = map(int, input().split())
    nodes = [[] for _ in range(100)]
    node_list= list(map(int, input().split()))
    '''
    graph = [[] for _ in range(100)]
    for i in range(N):
        graph[temp[2 * i]].append(temp[2 * i + 1])
    '''

    # 연결 리스트
    for i in range(0, len(node_list), 2):
        nodes[node_list[i]].append(node_list[i+1])

    start = 0
    end = 99
    def dfs(s, e):

        visited = [0] * 100
        stack = []
        stack.append(s)
        while len(stack):
            top = stack.pop()
            if top == e:
                return 1
            if visited[top] == 0:
                visited[top] = 1
            for w in range(len(nodes[top])):
                if visited[nodes[top][w]] == 0:
                    visited[nodes[top][w]] = 1
                    stack.append(nodes[top][w])
        return 0
    print('#{} {}'.format(tc, dfs(0, 99)))