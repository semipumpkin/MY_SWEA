import sys
sys.stdin = open("input.txt", "r")

def game_winner(a, b):

    # 1 가위 2 바위 3 보
    # 연산을 편하게 하기 위해 a[1]의 값이 더 클경우 바꿔줬음
    if a[1] > b[1]:
        a, b = b, a

    if a[1] == 1 and b[1] == 2:
        return b
    elif a[1] == 2 and b[1] == 3:
        return b
    elif a[1] == 1 and b[1] == 3:
        return a
    else:
        return a

def divide(items):
    if len(items) == 1:
        return items.pop()
    else:
        n = len(items)
        group1 = []
        group2 = []
        for i in range(n):
            if i < (n + 1) // 2:
                group1.append(items[i])
            else:
                group2.append(items[i])
        return game_winner(divide(group1), divide(group2))
        # return group1, group2

T = int(input())

'''
2  1  1 / 2  3  3
  2  1      3  3
    2        3
        3
'''
for tc in range(1, T+1):
    N = int(input())
    datas = list(map(int, input().split()))

    # data_list에 인덱스와 요소의 값을 리스트 형태로 저장해줌
    data_list = []
    for i in range(len(datas)):
        data_list.append([i + 1, datas[i]])
    # print(data_list)
    print('#{} {}'.format(tc, divide(data_list)[0]))
    # print(divide(data_list))