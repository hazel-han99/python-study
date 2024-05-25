import sys
input = sys.stdin.readline

n,m = list(map(int, input().split())) #숫자 n과 빈도수를 찾을 숫자 m 입력받기

cnt = 0

for i in range(1, n+1):
    cnt += str(i).count(str(m))

print(cnt)

'''
실버
시간복잡도 : O(n^2)이하, O(n)에서 끝내야함
str로 변환하는거 말고는 문제를 해결을 못하겠음.
'''