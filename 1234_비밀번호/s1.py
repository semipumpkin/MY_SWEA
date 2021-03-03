import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, nums = map(str, input().split())
    n = int(N)
    num_list = list(map(int, nums))
    # print(num_list)
    stack = ['.', '.']
    for i in range(len(num_list)):
        stack.append(num_list[i])
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    ans = ''.join(map(str, stack[2:]))
    print('#{}'.format(tc), ans)