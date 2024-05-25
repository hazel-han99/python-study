# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# n = int(input()) #n개의 사탕 입력받기
# #택희 ,영훈, 남규
# A, B, C = 0, 0, 0
#
# count = 0
#
# for i in range(1, 101):
#     if (n % i != 0 and C >= B+2 and A != 0 and B != 0 and C != 0):
#         candies = list(combinations(candies, 3))
#         count += 1
#         print(candies)

#print(count)

n = int(input())
s = 0
#택희가 가져갈 사탕이 짝수이기 때문에 인덱스 2부터 시작하여, 2씩 증가
for i in range(2, n-1, 2):
    s += (n-i-2)//2 #택희가 가져갈 i개의 사탕을(짝수를 만들기 위해 -2를 하고) n에서 뺀 것을 나머지 두 명이 가져가는 경우의 수
print(s)


'''
아이디어 : 조건문을 사용하고, 조합을 사용하자
combinations를 사용하려했으나, n은 배열이 아니기 때문에 어떻게 3개로 나눠야할지를 모르겠다
간단한 문제인줄 알았는데 생각보다 복잡하다. 조건을 조건문으로 줄 생각을 하지말고 전체 사탕의 수에서 미리 빼 두는것이 포인트였다.
'''