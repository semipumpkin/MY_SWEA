import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def binarysearch(a, key):
    start = 1
    end = a
    count = 0

    while start <= end:
        middle = (start + end) // 2

        if middle == key:
            break
        elif middle > key:
            end = middle
        else:
            start = middle
        count += 1

    return count

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    if binarysearch(P, A) > binarysearch(P, B):
        winner = 'B'
    elif binarysearch(P, A) < binarysearch(P, B):
        winner = 'A'
    else:
        winner = 0
    print('#{} {}'.format(tc, winner))