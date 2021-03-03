import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = input()
    strings = input()
    total = 0
    for s in strings:
        if s.isdigit():
            total += int(s)
    print('#{} {}'.format(tc + 1, total))


