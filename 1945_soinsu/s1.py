import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# N = int(input())
for i in range(1, T + 1):
    N = int(input())
    # print(N)
    # 이문제는 소인수가 이미 주어져서 난이도가 확 낮아진것 같다.
    abcde = [0] * 5
    soinsu = [2, 3, 5, 7, 11]

    # N이 1이 될때까지 소인수로 나눠질때 카운트를 올리고 N을 소인수로 나누는 것 ㅏㄴ복
    while N > 1:
        for j in range(len(soinsu)):
            if N % soinsu[j] == 0:
                abcde[j] += 1
                N = N / soinsu[j]
    #출력
    print('#{}'.format(i), end=" ")
    for k in range(5):
        print(abcde[k], end=" ")
    print()





