import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))
    i = 1
    while True:
        Q = nums.pop(0)
        if Q - i> 0:
            nums.append(Q - i)
            i += 1
            if i == 6:
                i = 1
        else:
            nums.append(0)
            # nums.append(nums.pop)
            break

    print('#{}'.format(tc),*nums)