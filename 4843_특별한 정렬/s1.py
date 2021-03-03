import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    num_list = list(map(int, input().split()))
    for i in range(N):
        for j in range(i + 1, N):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    strange_sorted = []
    while len(strange_sorted) < 10:
        strange_sorted += [num_list[-1]]
        strange_sorted += [num_list[0]]

        num_list.pop(-1)
        num_list.pop(0)
        # print(num_list)
        
    print('#{}'.format(tc), *strange_sorted)

