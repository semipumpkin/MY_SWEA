import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    count = [0] * len(str1)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count[i] += 1
    max_num = count[0]
    for num in count:
        if num > max_num:
            max_num = num
    print('#{} {}'.format(tc, max_num))



