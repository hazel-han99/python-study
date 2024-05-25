import sys
input = sys.stdin.readline

n = int(input()) #불꽃 n개 입력받기

for i in range(1, n+1):
    if (1 + i + i ** 2 == n) : print(i)