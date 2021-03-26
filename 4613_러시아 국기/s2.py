import sys
sys.stdin = open("input.txt", "r")

def perm(idx, sub_sum):
    global ans
    # 유망성 검사. 아래의 조건문에 걸리게 되면 이후 작업은 의미가 업슴
    if sub_sum > N:
        return
    if idx == 3:
        if sub_sum == N:
            cnt = 0

            start = sel[0]
            start2 = start+sel[1]

            # 흰색 칠하기
            for i in flag[:start]:
                for j in i:
                    if j != 'W':
                        cnt += 1

            # 파란색 칠하기
            for i in flag[start: start2]:
                for j in i:
                    if j != 'B':
                        cnt += 1

            for i in flag[start2: ]:
                for j in i:
                    if j != 'R':
                        cnt += 1
            if ans > cnt:
                ans = cnt
        return

    # 중복 순열 살짝 응용
    for i in range(1, N - 1):
        sel[idx] = i
        perm(idx+1, sub_sum + i)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 1000000
    flag = [list(input()) for _ in range(N)]
    sel = [0] * 3

    print(perm(0, 0))