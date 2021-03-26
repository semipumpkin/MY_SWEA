import sys
sys.stdin = open("input.txt", "r")

def jegob(n, m):

    if m == 0:
        return 1
    else:
        m -= 1
        return n*jegob(n, m)

for _ in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())
    # print('#{} {}'. format(tc, jegob(N, M)))
def dec_to_bin(N):
    result = ''
    if N <= 1:
        result += '0'
        return result
    else:
        pass



# print(dec_to_bin(8))
def go(index):
    if index >= 3:
        print(*result)
        return
    result.append(data[index])
    go(index + 1)
    result.pop()

    go(index + 1)

data = [i for i in range(1, 4)]
result = []
go(0)
# https://realpython.com/python-thinking-recursively/#dear-pythonic-santa-claus