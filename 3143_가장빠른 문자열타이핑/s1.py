import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    a, b = map(str, input().split())

    for i in range(len(a) - len(b)):
        if a[i: i+len(b)] == b:
            a = a.replace(a[i:i+len(b)], '.')
    print('#{} {}'.format(tc, len(a)))