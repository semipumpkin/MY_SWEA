import sys
sys.stdin = open("input.txt", "r")

Tn = int(input())

for i in range(1, 4):
    Ti = int(input())
    Li = list(map(int, input().split()))
    max_value = 0
    for j in range(1, Ti):
        if max_value < Li[j]:
            max_value = Li[j]
    min_value = 10000000
    for j in range(1, Ti):
        if min_value > Li[j]:
            min_value = Li[j]
    print('#{} {}'.format(i, max_value - min_value))