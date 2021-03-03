import sys
sys.stdin = open("input.txt", "r")
sys.stdin = open("input.txt", 'rt', encoding='UTF8')
def find_word_1(target, words):

    count = 0

    # 들어온 문자열 words를 탐색
    for i in range(len(words) - len(target) + 1):

        # 각 문자열마다 비교할 문자를 만듦
        compare = ''

        # i번째 문자열부터 target 문자의 숫자만큼 비교할 문자를 만들어줌
        for j in range(i, i + len(target)):
            compare += words[j]

        # 비교할 문자가 target과 같다면 count + 1
        if compare == target:
            count += 1
    return count


for _ in range(10):
    num = int(input())
    target = input()
    strings= input()
    print('#{} {}'.format(num, find_word_1(target, strings)))
