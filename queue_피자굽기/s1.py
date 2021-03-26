import sys
sys.stdin = open("input.txt", "r")




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    Q = [0] * N
    front, rear = 0, 0



