import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    macdae = input()


    # for i in range(len(macdae) - 1):
    #         if macdae[i] == '(' and macdae[i + 1] != ')':
    #             total += 1
    # 처음 막대의 개수
    total = 0

    # 현재 처형대 위에 있는 막대의 갯수
    cur_count = 0

    # 잘려진 막대의 갯수
    cut = 0

    for i in range(len(macdae) - 1):

        # 포문을 돌며 레이저를 만나면 잘려진 막대의 개수에 더해줌
        if macdae[i] == '(' and macdae[i + 1] != ')':
            cur_count += 1
            total += 1

        # 그리고 레이저 다음에 )가 나타나면 잘려진 현재 처형대 위에 있는 막대만큼 더해주고
        if macdae[i] == '(' and macdae[i + 1] == ')':
            cut += cur_count

        # 처형대 위에 있는 막대를 빼줌
        elif macdae[i] == ')' and macdae[i + 1] == ')':
            cur_count -= 1

    # 처음 막대의 개수와 잘려진 막대의 개수를 더하면 총 잘려진 막대의 개수를 구할 수 있음
    print('#{} {}'.format(tc, total + cut))



s = []
ans = 0
for i in range(len(macdae)):
    if macdae[i] == '(':
        s. append('(')
    else:
        s.pop()
        if macdae[i - 1] == '(':
            ans += 1
        else:
            ans += 1

    print('#[] []'.format(tc, ans))

