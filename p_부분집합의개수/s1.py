# 6개의 원소가 담긴 리스트
nums = [3, 6, 7, 1, 5, 4]
# 리스트의 크기
n = len(nums)
# 부분집합의 개수를 더해 갈 변수
cnt = 0
for i in range(1 << n): # 모든 부분집합의 개수만큼 반복
    cnt = 0
    for j in range(n): # 리스트의 원소 개수만큼 반복 /  j가 필요한 이유? 원 집합의 인덱스!
        if i & (1 << j): #
            print(nums[j], end = ' ')
    print(cnt)

