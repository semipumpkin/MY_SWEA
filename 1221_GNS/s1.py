import sys
sys.stdin = open("input.txt", "r")
#
def sorting(nums):
    # 문자로 된 숫자들의 리스트를 만듦
    nums_char = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # 그 갯수만큼 카운팅 리스트를 만듬. 카운팅 리스트의 인덱스는 문자로 된 숫자들의 값과 대응 됨
    count = [0] * 10

    # nums의 문자를 돌며 count 리스트에 count를 추가해줌
    for i in range(len(nums_char)):
        count[i] += nums.count(nums_char[i])

    # count리스트의 요소만큼 문자로 된숫자들을 리스트에 더해줌
    result = []
    for i in range(len(count)):
        result += [nums_char[i]] * count[i]
    return result
    # nums_char 를 돌며 각 인덱스에 해당하는 요소를 count 인덱스에 해당하는 count 수만큼 리스트에 더해줌
T = int(input())



for tc in range(1, T + 1):
    M, N = map(str, input().split())
    words = list(map(str, input().split()))
    print(M)
    print(*sorting(words))

