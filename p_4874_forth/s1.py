import sys
sys.stdin = open("input.txt", "r")

# 숫자 스택
# 연산자를 만나면 스택 숫자 두개 꺼내서 더하고 다시 스택
# '.'은 스택에서 숫자를 꺼내 출력
# 연산불가 'error'
def forth(data):
    stack = []

    # 숫자면 스택에 쌓음
    for i in range(len(data)):
        if data[i].isdigit():
            stack.append(int(data[i]))

        # '.' 만나면 출력
        elif data[i] == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'

        else:
            if len(stack) >= 2:
                num1 = stack.pop()
                num2 = stack.pop()
                if data[i] == '+':
                    stack.append(num1 + num2)
                elif data[i] == '-':
                    stack.append(num2 - num1)
                elif data[i] == '/':
                    stack.append(num2 // num1)
                elif data[i] == '*':
                    stack.append(num1 * num2)
            else:
                return 'error'

T = int(input())
for tc in range(1, T+1):
    datas = input().split()
    print('#{} {}'.format(tc, forth(datas)))
