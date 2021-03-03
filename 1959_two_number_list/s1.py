import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # M이 N보다 클때
    if M > N:
        # 총합 리스트를 만들어주고
        total_list = []

        # B 리스트를 돌며
        for i in range(M - N + 1):

            # A의 갯수만큼 슬라이싱 후
            sliced = B[i : i + N]
            total = 0

            # 같은 인덱스 숫자끼리 곱해서 곱한 값의 합을 total에 저장
            for j in range(N):
                total += sliced[j] * A[j]
            # 저장한 total을 총합 리스트에 저장
            total_list += [total]
    # A B 반대로
    else:
        total_list = []
        for i in range(N - M + 1):
            sliced = A[i: i + M]
            total = 0
            for j in range(M):
                total += sliced[j] * B[j]
            total_list += [total]

    # 총합 리스트에서 제일 큰수 뽑기
    max_v = total_list[0]
    for i in range(len(total_list)):
        if max_v < total_list[i]:
            max_v = total_list[i]

    print('#{} {}'.format(tc, max_v))