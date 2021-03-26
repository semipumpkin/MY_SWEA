def move(no, x, y):
    global count
    global total
    '''원반 no개를 x기둥에서 y기둥으로 옮김'''
    if no > 1:
        # 1) 맨 밑 원반을 제외한 그 위의 원반을 중간 기둥으로 옮김
        move(no - 1, x, total*2 - x - y)  # 중간 기둥의 번호 = 6-시작기둥-목표기둥
    # 2) 바닥의 원반을 목표 기둥으로 옮김(말로만 표현)
    print(x, y)
    count += 1

    if no > 1:
        # 3) 중간 기둥에 있는 나머지 원반들을 목표 기둥으로 옮김
        move(no - 1, total*2 - x - y, y)
def t(no, x, y):
    global count
    global total
    '''원반 no개를 x기둥에서 y기둥으로 옮김'''
    if no > 1:
        # 1) 맨 밑 원반을 제외한 그 위의 원반을 중간 기둥으로 옮김
        t(no - 1, x, total*2 - x - y)  # 중간 기둥의 번호 = 6-시작기둥-목표기둥
    # 2) 바닥의 원반을 목표 기둥으로 옮김(말로만 표현)
    # print(x, y)
    count += 1

    if no > 1:
        # 3) 중간 기둥에 있는 나머지 원반들을 목표 기둥으로 옮김
        t(no - 1, total*2 - x - y, y)

    # count += 1
count = 0
total = int(input())
t(total, 1, total)
print(count)
move(total, 1, total)

