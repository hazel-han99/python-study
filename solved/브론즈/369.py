import sys
#input = sys.stdin.readline()

# n = int(input()) #특정 수 n을 입력받기
# result = []
# count = 0
#
# #1부터 입력받은 n까지 반복하면서
# for i in range(1, n+1):
#     if ('3' in str(i) or '6' in str(i) or '9' in str(i)): #현재 인덱스에 3, 6, 9 중 하나라도 포함되어있으면 result 리스트에 저장
#         result.append(i)
#         continue #다음 반복 실행
#
# for j in result:
#     jSplit = list(map(int, str(j)))
#     if (jSplit == 3 or jSplit == 6 or jSplit == 9):
#         count +=1
#
# print(count)

N = int(input())
check = '369'
re = 0
for i in range(1, N+1):
    str_num = str(i)
    for c in check:
        re += str_num.count(c)
print(re)

#count함수를 사용해볼까했지만 조건을 하나밖에 넣을 수 없어서 사용할 수 없다
#알게된점 : '369'를 count함수에 전달하여 for문으로 넣으면 3개를 돌릴 수 있다

# ++ count랑 str(i)없이 풀어보자
