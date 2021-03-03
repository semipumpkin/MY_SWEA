import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    strings = input()
    # 괄호 다시풀어보기
    stack = []
    result = 1
    for string in strings:
        if string == '{' or string == '(':
            stack.append(string)
        elif string == '}' or string == ')':
            if stack:

                # 괄호 짝꿍이 있는 경우
                if string == ')' and stack[-1] == '(':
                    stack.pop()
                elif string =='}' and stack[-1] == '{':
                    stack.pop()

                # 닫는 괄호가 없을 경우
                else:
                    result = 0
                    break
            # 여는 괄호 없이 닫는 괄호가 나온 경우
            else:
                result = 0
                break
    # print(stack)
    if stack:
        result = 0
    print('#{} {}'.format(tc, result))