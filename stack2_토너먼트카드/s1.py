import sys
sys.stdin = open("input.txt", "r")
#
# def winner(nums):
#     result = []
#     if len(nums) == 1:
#         return nums
#     else:
#         while nums:
#             t1 = nums.pop(0)
#             if not nums:
#                 result.append(t1)
#                 break
#             t2 = nums.pop(0)
#
#
#             if t1[1] == 1:
#                 if t2[1] == 3:
#                     result.append(t1)
#                 elif t2[1] == 2:
#                     result.append(t2)
#                 elif t2[1] == 1:
#                     if t1[0] < t2[0]:
#                         result.append(t1)
#                     else:
#                         result.append(t2)
#             elif t1[1] == 2:
#
#                 if t2[1] == 1:
#                     result.append(t1)
#                 elif t2[1] == 3:
#                     result.append(t2)
#                 elif t2[1] == 2:
#                     if t1[0] < t2[0]:
#                         result.append(t1)
#                     else:
#                         result.append(t2)
#             elif t1[1] == 3:
#                 if t2[1] == 2:
#                     result.append(t1)
#                 elif t2[1] == 1:
#                     result.append(t2)
#                 elif t2[1] == 3:
#                     if t1[0] < t2[0]:
#                         result.append(t1)
#                     else:
#                         result.append(t2)
#     return winner(result)
#


T = int(input())

'''
2  1  1 / 2  3  3
  2  1      3  3
    2        3
        3
'''
for tc in range(1, T+1):
    N = int(input())
    datas = list(map(int, input().split()))
    # print(datas)
    data_list = []
    for i in range(len(datas)):
        data_list.append([i + 1, datas[i]])

    print(data_list)

# 1 가위 2 바위 3 보



# 그룹을 두개 나누고
# 이긴사람을 스택에 쌓고 비교하는 방식으로 가자
# 애초에 스택을 저장할때 번호도 같이 저장하자.
#     group1 = []
#     group2 = []
    for i in range(len(datas)):
        if i < len(datas) // 2:
            group1.append([i, datas[i]])
        else:
            group2.append([i, datas[i]])
#     # print(group1, '///', group2)
#     # print(winner(group1), '///', winner(group2))
#     # final1 = winner(group1)
#     # final2 = winner(group2)
#     final = winner(group1) + winner(group2)
#     print('#{} {}'.format(tc, winner(final)[0][0] + 1))

