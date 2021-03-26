


def fibo(n):
    if not n:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

N = int(input())
print(fibo(N))