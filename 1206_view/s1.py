import sys
sys.stdin = open("input.txt", "r")

T1 = int(input())
cng1 = list(map(int, input().split()))
T2 = int(input())
cng2 = list(map(int, input().split()))
T3 = int(input())
cng3 = list(map(int, input().split()))
T4 = int(input())
cng4 = list(map(int, input().split()))
T5 = int(input())
cng5 = list(map(int, input().split()))
T6 = int(input())
cng6 = list(map(int, input().split()))
T7 = int(input())
cng7 = list(map(int, input().split()))
T8 = int(input())
cng8 = list(map(int, input().split()))
T9 = int(input())
cng9 = list(map(int, input().split()))
T10 = int(input())
cng10 = list(map(int, input().split()))

# 앞뒤 2칸과 비교
def jomang(cng):
    jo = 0
    for i in range(2, len(cng) - 2):
        if cng[i] > cng[i - 2] and cng[i] > cng[i - 1] and cng[i] > cng[i + 1] and cng[i] > cng[i + 2]:
            jo += cng[i] - max([cng[i -2], cng[i - 1], cng[i + 1], cng[i + 2]])
    return jo
print( '#{} {}'.format(1, jomang(cng1)))
print( '#{} {}'.format(2, jomang(cng2)))
print( '#{} {}'.format(3, jomang(cng3)))
print( '#{} {}'.format(4, jomang(cng4)))
print( '#{} {}'.format(5, jomang(cng5)))
print( '#{} {}'.format(6, jomang(cng6)))
print( '#{} {}'.format(7, jomang(cng7)))
print( '#{} {}'.format(8, jomang(cng8)))
print( '#{} {}'.format(9, jomang(cng9)))
print( '#{} {}'.format(10, jomang(cng10)))
