import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    macdae = input()
    # print(macdae)

    # () ((( ()() )( () ) () ))( () )
    stack = []

    # 총 막대의 수
    answer = 0

    # macdae 돌면서
    for i in range(len(macdae)):

        # '('를 만나면 스택에 더해줌
        if macdae[i] == '(':
            stack.append(macdae[i])

        # 그 외의 요소 ')' 를 만나면
        else:
            # 그 전 요소가 '('이면 레이져
            if macdae[i - 1] == '(':

                # 따라서 레이져에 해당하는 열린 막대를 stack에서 빼주고
                stack.pop()

                # len(stack)은 그동안 쌓인 막대를 의미 = 판 위에 있는 막대기들의 수
                # 레이져를 만나면 그동안 쌓인 막대의 수만큼 잘려짐
                answer += len(stack)

            # 만약 레이져를 만나지 않는다면 쇠막대가 끝났다는 의미
            else:

                stack.pop() # 그렇기 때문에 스택에서 '('를 빼줌

                # 그동안 잘려진 막대의 수만 더했기 때문에 쇠막대기가 끝나면 남은 조각들을 더해줌
                answer += 1

    print('#{} {}'.format(tc, answer))

