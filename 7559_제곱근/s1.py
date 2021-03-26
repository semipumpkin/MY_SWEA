import sys
sys.stdin = open("input.txt", "r")

def binary_search(n):
    end = n
    start = 0
    mid = (end + start)//2
    while mid**2 != n:
        if mid**2 > n:
            end = mid
            mid = (end + start)//2
        else:
            start = mid
            mid = (end + start)//2
    return mid

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(binary_search(N))