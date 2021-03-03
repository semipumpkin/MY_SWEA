import sys
sys.stdin = open('input.txt')

test_case = 10
for tc in range(test_case):
    N = int(input())
    word = input()
    stack = []
    # 후위표기식으로 표현하여 result에 넣기
    result = []
    for idx in range(len(word)):
        # 숫자라면 int형으로 변경 후에 result에 넣기
        if word[idx].isdecimal():
            number = int(word[idx])
            result.append(number)
        # 연산자일 때
        else:
            if word[idx] == '+':
                # 덧셈일 때 스택이 빌 때까지 result에 pop하기
                while stack:
                    result.append(stack.pop())
                # 이후 스택에 + 넣기
                stack.append(word[idx])
            elif word[idx] == '*':
                # 곱셈일 때 스택이 비거나 덧셈이 나올 때까지 result에 pop하기
                while stack and stack[-1] == '*':
                    result.append(stack.pop())
                # 이후 스택에 * 넣기
                stack.append(word[idx])
    print(stack, result)
    # 남은 연산자들 result에 pop
    # while stack:
    #     result.append(stack.pop())
    # stack = []
    # answer = 0
    # for idx in range(len(result)):
    #     # 연산자일 경우 숫자를 넣은 스택에서 2개를 꺼내어 연산하기
    #     if result[idx] == '+':
    #         x = stack.pop()
    #         y = stack.pop()
    #         stack.append(x+y)
    #     elif result[idx] ==  '*':
    #         x = stack.pop()
    #         y = stack.pop()
    #         stack.append(x*y)
    #     # 숫자일 경우 스택에 push
    #     else:
    #         stack.append(result[idx])
    # print("#{} {}".format(tc+1, stack[0]))
