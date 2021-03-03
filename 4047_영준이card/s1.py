import sys
sys.stdin = open("input.txt", "r")

# A는 1, J, Q, K 는 11, 12, 13

# 무늬별로 각각 13장씩
T = int(input())

for tc in range(1, T+1):

    cards = input()
    # 문양마다 counting list, 13 만듬

    # 에러 먼저 판별
    compare = []
    for i in range(len(cards)):

        # 카드의 문양만 compare에 저장해서 카드의 수와 같다면 break
        compare += [cards[i*3: (i + 1)*3]]
        if len(compare) == len(cards) // 3:
            break

    # 저장한 문양에서 같은 문양이 2개 이상이면 에러
    for card in compare:
        if compare.count(card) >= 2:
            print('#{} {}'.format(tc, 'ERROR'))
            break
        else:
            pass

    # 이제 중복되지 않은 카드들만 남았으니 카운팅 리스트에서 해당하는 문양들의 카드의 갯수를 빼주면 답
    else:
        cnt_list = [13] * 4
        for i in range(len(compare)):
            if cards[i*3] == 'S':
                cnt_list[0] -= 1
            elif cards[i*3] == 'D':
                cnt_list[1] -= 1
            elif cards[i*3] == 'H':
                cnt_list[2] -= 1
            elif cards[i*3] == 'C':
                cnt_list[3] -= 1
        print('#{}'.format(tc), *cnt_list)