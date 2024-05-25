import sys
input = sys.stdin.readline()

n, k = map(int, input.rstrip().split()) #공백으로 구분하여 map형태로 저장
divisorNumbers = [] #약수들을 넣을 빈 리스트 생성

#약수들을 리스트에 저장
for i in range(1, n+1):
    if (n % i == 0):
        divisorNumbers.append(i)

#divisorNumbers.sort() #리스트를 오름차순으로 정렬 -> 원래 오름차순이라 안넣어도됨
print(divisorNumbers)

#n의 약수의 개수가 k보다 크면,
if (len(divisorNumbers) > k):
    print(divisorNumbers[k]) #k번째 약수 출력
else: print(0) #아니면, 0출력

#시간복잡도 : O(n)?
# ++ 배열사이즈 조절 문제 12번 라인 이후의 문제
