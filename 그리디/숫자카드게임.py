import sys
#input = sys.stdin.readline().rstrip

#아이디어 : 각 행마다 가장 작은 수를 찾고, 그 중에 가장 큰 수를 찾으면 된다.

print("행과 열을 입력해주세요.")
n, m = map(int, input().split()) #공백으로 분리하여 행, 열 입력받기

result = 0 #결과값 선언 및 초기화

for i in range(n) :
    cardList = list(map(int, input().split()))
    min_value = min(cardList) #현재 입력받은 것 중에 가장 작은 값 min_value에 대입
    result = max(result, min_value) #min_value 중 큰 값 result에 대입

print(result)

