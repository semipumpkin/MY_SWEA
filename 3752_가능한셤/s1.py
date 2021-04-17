import sys
sys.stdin = open('1.txt', 'r')

'''
2 3 5


'''

# def possible_score(idx):
#     # global total
#
#     if idx == N:
#         total = sum(visited)
#         if total not in result:
#             result.append(total)
#
#         return
#     possible_score(idx+1)
#     visited.append(scores[idx])
#     possible_score(idx+1)
#     visited.pop()
    # total += scores[idx]
    # for i in range(idx, N):
    #     if visited[i] == 0:
    #         visited[i] = 1
    #         possible_score(idx+1, total + scores[i])
    #         visited[i] = 0
    #         possible_score(idx+1, total + scores[i])

def go(idx, total):
    if idx == N:
        result.add(total)
        return



    # if total in result:
    #     return

    go(idx+1, total+scores[idx])
    go(idx+1, total)


for tc in range(1, int(input())+1):
    N = int(input())
    scores = list(map(int, input().split()))
    # visited = []
    count = 0
    # for _ in range(N):
    #     scores.append(0)
    # print(scores)
    result = set()
    # possible_score(0)
    go(0, count)
    # print(result)
    # print(result)
    print('#{} {}'.format(tc, len(result)))