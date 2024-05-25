import sys

# n = list(int(input()))
#
# for i in n:
#     for j in i:
#         n[i]

from itertools import combinations
import sys
input = sys.stdin.readline

# 입력
numlist = [ int(input()) for _ in range(9)]

# 9개 중 7개를 뽑을 조합
case = list(combinations(numlist, 7))

# 합이 100이 되면
for i in case:
    if sum(i) == 100:
        #원소들을 하나씩 출력해야해서 또 반복문을 사용한듯
        for j in i:
            print(j)


#반복문을 사용하여 풀까, 조합을 사용해야하나 했는데 뭔가 사용할 수 있는 함수가 있을거라는 생각이 들어서 답지를 봤다
#저번 블랙잭 문제 때처럼 조합으로 뽑아서 합계를 구하면 되는데 생각을 못했다..