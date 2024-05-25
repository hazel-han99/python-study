'''import sys
input = sys.stdin.readline

n, kim, lim = input().split()

print(n, kim, lim)'''

'''
실버
시간복잡도 : O(n) 안에서 끝내야함.
아예 접근을 못하겠다
깨달은 점 : map으로 세 개 이상의 원소를 받을 수 있구나
그냥 다른 번호들보다는 주인공들의 점수에 초점을 맞춰서 같아질 때만 찾으면 되는 간단한 문제였다
'''

import sys
input = sys.stdin.readline

# 입력
N, a, b = map(int, input().split())

# 토너먼트
cnt = 0
while a != b:
    a -= a // 2
    b -= b // 2
    cnt += 1
print(cnt)