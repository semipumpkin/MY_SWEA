import sys
sys.stdin = open("input.txt", "r")


def ninety(box):
    result = []
    for y in range(N):
        tmp = []
        for x in range(N-1, -1, -1):
            tmp.append(box[x][y])
        result += [''.join(map(str, tmp))]
    return result

'''     90     
1 2 3  7 4 1   
4 5 6  8 5 2  
7 8 9  9 6 3   

3 6 9
6 5 8
3 6 3

1 2 3 4        13 9 5 1 
5 6 7 8        14 10 6 2
9 10 11 12     15 11 7 3
13 14 15 16    16 12 8 4
'''









T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    oneeighty = ninety(ninety(matrix))
    twoseventy = ninety(oneeighty)
    print('#{}'.format(tc))
    for i in range(N):
        print('{} {} {}'.format(ninety(matrix)[i], oneeighty[i], twoseventy[i]))