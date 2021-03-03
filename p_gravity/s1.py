import sys
sys.stdin = open("input.txt", "r")

T = int(input())

N = int(input())

b = list(map(int, input().split()))

cnt_list = [0] * N
def gravity(size, box):
    for i in range(size):
        for j in range(i + 1, size):
            if box[i] > box[j]:
                cnt_list[i] += 1
    return max(cnt_list)


for tc in range(1, T+1):
    print('#{} {}'.format(tc, gravity(N, b)))
