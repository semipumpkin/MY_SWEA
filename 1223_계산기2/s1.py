import sys
sys.stdin = open('input.txt')

def yeonsan(N, s):
    stack = []
    nums = ''
    num_list = []
    yeonsanja = {'+': 1, '*': 2}

    # 1. 중위표현식 > 후위표현식
    for i in range(N):
        if 48 <= ord(s[i]) <= 57: # 숫자이면
            nums += s[i]
        else: # 숫자가 아니고
            if not stack: # 스택이 비어있으면
                stack.append(s[i]) # 스택에 넣자
            else: #스택이 비어있지 않으면
                if yeonsanja[s[i]] > yeonsanja[stack[-1]]: # 우선순위가 높으면
                    stack.append(s[i]) # 스택에 쌓자
                else: # 우선 순위가 낮으면
                    # 우선 순위가 높은게 나오거나, 스택이 비기 전까지
                    # 스택에 쌓인 연산자를 nums에 붙여라
                    while stack and yeonsanja[s[i]] <= yeonsanja[stack[-1]]:
                        nums += stack.pop()
                    stack.append(s[i]) # 위 반복문을 나온 후 스택에 값을 추가해라
    print(stack)
    # 남아 있는거 털어라
    for i in range(len(stack)):
        nums += stack.pop()


    # 2. 후위표현식 > 계산
    for i in range(len(nums)):
        if 48 <= ord(nums[i]) <= 57: # 숫자이면
            num_list.append(int(nums[i]))
        elif nums[i] == '+': # + 가 나오면 더하고
            a = num_list.pop()
            b = num_list.pop()
            num_list.append(a+b) #
        else: # * 이 나오면 곱해라
            b = num_list.pop()
            num_list[-1] *= b

    return num_list.pop()


for tc in range(1, 11):
    N = int(input())
    s = input()
    print('#{} {}'.format(tc, yeonsan(N, s)))