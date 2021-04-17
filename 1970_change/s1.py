import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    don = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8
    print('#{}'.format(tc))
    for i in range(len(don)):
        # if N // don[i]:
        cnt[i] = N // don[i]
        print(cnt[i], end=" ")
        N %= don[i]
            # N //= 10
    # for j in range(len(cnt)):
    print()

