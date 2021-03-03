import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# N = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N의 범위의 소수를 찾는다
    sosu = []
    for i in range(1, N + 1):
        # N의 범위의 숫자를 하나씩 돌며 약수를 구함
        yak = []
        for j in range(1, i + 1):
            if i % j == 0:
                yak += [j]

        # 약수의 집합의 길이가 2라는 것은 약수가 1과 그 자신뿐이라는 것을 의미. 즉, 소수
        if len(yak) == 2:
            # 소수를 소수 집합에 넣음
            sosu += [yak[1]]

    # 소수중에서 N의 소인수를 구함
    soinsu = []
    for i in range(len(sosu)):
        if N % sosu[i] == 0:
            soinsu += [sosu[i]]
    soinsu_cnt = [0] * (len(soinsu))


    while N > 1:
        for j in range(len(soinsu)):
            if N % soinsu[j] == 0:
                soinsu_cnt[j] += 1
                N = N / soinsu[j]

    print('#{}'.format(tc), end=" ")
    for k in range(len(soinsu)):
        print(soinsu_cnt[k], end=" ")
    print()



