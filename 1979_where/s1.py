import sys
sys.stdin = open("input.txt", "r")




def count_found(N, K, box):
    word_count = 0
    for y in range(N):
        one_count = 0
        for x in range(N):
            if box[y][x] == 1:
                one_count += 1
            else:
                if one_count == K:
                    word_count += 1
                one_count = 0
    for y in range(N):
        for x in range(N):
            box[y][x] = box[x][y]

    # 행렬 변형 공부!


    return word_count

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    box = [ list(map(int, input().split())) + [0] for _ in range(N)]
    print(count_found(N, K, box))
