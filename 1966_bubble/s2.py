import sys
sys.stdin = open("input.txt", "r")

def Quick(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        left = []
        right = []
        pivot = numbers[0]

        for i in range(1, len(numbers)):
            if numbers[i] <= pivot:
                left.append(numbers[i])
            else:
                right.append(numbers[i])
        return [*Quick(left), pivot, *Quick(right)]




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    print('#{}'.format(tc), *Quick(num_list))