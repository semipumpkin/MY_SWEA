import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    datas = input()
    stack = []
    result = ''
    for data in datas:

        # 숫자일 때 넣기
        if data.isdigit():
            result += data

        # 여는 괄호일때 연산자에 넣기
        elif data == '(':
            stack.append(data)

        # 닫는 괄호일때, 여는 괄호가 나올때까지 쭉 넣기
        elif data == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        # 곱셈연산자일때, 다음 곱셈 연산자가 나올때까지 넣어줌
        elif data == '*':
            while stack[-1] == '*':
                result += stack.pop()
            stack.append(data)

        # 덧셈연산자일때, 여는 괄호가 나올때까지 넣어줌
        elif data == '+':
            while stack[-1] != '(':
                result += stack.pop()
            stack.append(data)
    print(result)

    nums = []
    for i in range(len(result)):
        if result[i].isdigit():
            nums.append(int(result[i]))
        else:
            a = nums.pop()
            b = nums.pop()
            if result[i] == '+':
                nums.append(b+a)
            elif result[i] == '*':
                nums.append(b*a)
    print('#{} {}'.format(tc, nums.pop()))
