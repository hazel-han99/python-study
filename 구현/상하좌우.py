import sys

# n = int(input()) #공간의 크기를 나타내는 n 입력받기
#
# area = [n, n]
#
# control = [L, R, U, D]
#
# if (control == L)
#     area[1] = area[1]-1
# elif (control == R)
#     area[1] = area[1]+1
# elif (control == U)
#     area[0] = area[0]-1
# elif (control == D)
#     area[0] = area[0]+1
#
# print(area)

#include <bits/stdc++.h>

# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)