# import sys
# from itertools import combinations
#
# input = sys.stdin.readline()
#
# cardCount = int(input.rstrip().split())#카드의 수 입력받기
# examNumber = int(input.rstrip().split())#예시 숫자 입력받기
#
# #입력받은 카드 수만큼 반복하여, 카드 숫자 입력받기
# for cards in range(cardCount):
#     cardList = int(list(map(int,  input().split())))
#
# #3개를 뽑는 모든 조합 생성
# cardCombination = list(combinations(cardList,3))
#
# print(cardCombination)
#
# for i in cardCombination:
#     min_result = examNumber % i
#     if (min_result > )

from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
nlst = [] #합계를 담을 빈 리스트를 선언

for three in combinations(lst, 3):
    if sum(three) > M:
        continue
    else:
        nlst.append(sum(three))
print(max(nlst))

#배운점 : map을 이용하여 입력받기, sum 함수 사용하기, 반복문 자체 범위에 combinations 사용하기
#잘못 생각한 점 : 조합으로 뽑는건 알겠는데, 그걸 리스트에 담아서 어떻게 합계를 구하나 고민하고 있었다, 시간복잡도를 생각하지 못했다