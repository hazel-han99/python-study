import sys
input = sys.stdin.readline

n = int(input())
sum = 0

for i in range(1, n+1):
    if (n % i == 0):
        sum += i

print(sum*5-24)

#시간복잡도 O(n)