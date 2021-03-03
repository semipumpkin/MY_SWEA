import sys
sys.stdin = open("input.txt", "r")


def combination(n, k):
    if k == 0 or k == n:
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k)

def pascals_triangle(num):
    for y in range(num):
        answer = ''
        for x in range(y + 1):
            answer = answer + str(combination(y, x)) + " "
        # print(answer)
    return answer
    # 1
    # 1 1  [pascal(0)[0]] + [pascal(0)[1]]
    # 1 2 1 [pascal(1)[0]] + [pascal(1)[0] + pascal(1)[1]] + [pascal(1)[-1]]
    # 1 3 3 1 [pascal(2)[0]] + [pascal(2)[0] + pascal(2)[1]] + [pascal(2)[1] + pascal(2)[2]] + [pascal(2)[-1]]
    # 1 4 6 4 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(1, N+1):
        print(pascals_triangle(i))
