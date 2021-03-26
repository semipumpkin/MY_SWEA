import sys
sys.stdin = open("input.txt", "r")

def promising(nums):
    result = []

    # return mat

def pick(idx):
    global min_mat
    if idx == N:
        if sel.count(1) == 2:
            # if promising(total) < min_mat:
            #     min_mat = promising(total)
            # print(total)
            print(sel)
            return

    else:
        sel[idx] = 1
        pick(idx+1)
        sel[idx] = 0
        pick(idx+1)



T = int(input())
for tc in range(1, 2):
    N = int(input())
    synergy = [ list(map(int, input().split())) for _ in range(N) ]

    min_mat = 100000000000
    sel = [0] * N
    pick(0)
