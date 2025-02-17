#가장 큰 데이터와 가장 작은 데이터의 차이가 100만을 넘지 않을 때 효과적으로 사용할 수 있다
#데이터의 크기가 한정되어있고, 동일한 값이 중복될수록 적합
#O(N + K) N : 데이터의 개수, K : 데이터 중 최대값의 크기

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력