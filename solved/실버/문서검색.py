# import sys
# input = sys.stdin.readline()
#
# document = []
# word = []
# document.append(list(input.rstrip()))
# word.append(list(input.rstrip()))
#
# result = 0
#
# for i in word:
#     for j in document:
#         if (document[0] & word[i] != document[j]) : continue
#         if (document[0] & word[i] == document[j]):
#             if (word[i] != document[j]):
#                 continue;
#                 result+=1
#
# print(result)

#내장함수 사용 방법
# text = input()
# word = input()
# print(text.count(word))

#2번째 방법
data = input()
target = input()
start = 0
count = 0

while start <= len(data) - len(target):
    if data[start:start+len(target)] == target:
        count += 1
        start += len(target) #단어가 중복되지 않게 하기 위해서!
    else:
        start += 1 #원하는 문자열이 없다면 한칸씩 옆으로 이동

print(count)

#count함수를 사용하면 간단하게 중복을 제거하여서도 해결할 수 있다
#내가 생각하려던 방법 : 인덱스 하나씩 거치면서 단어가 같으면 계속 검사하다가 달라지는 순간에 카운트 1업 -> 카운트 숫자 출력
#처음엔 중복이라는 키워드 때문에 튜플?을 사용해야되나 생각도 했고, 슬라이싱을 해야되나 생각했었음

# ++ 중복을 허용했을 때는 어떻게 해야할지 생각해보자
