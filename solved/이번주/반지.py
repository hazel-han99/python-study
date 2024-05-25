import sys
input = sys.stdin.readline

order = input().rstrip() #문자열 입력받기
n = int(input()) #반지의 개수 입력받기

sentence = ''
cnt = 0

for _ in range(n):
    sentence = (input().rstrip()) * 2
    if (order in sentence): cnt += 1

print(cnt)

'''
실버
한 문장에 1개 이상이 있어도 카운트가 1번이고,
끝까지 가면 다시 첫 번째 인덱스부터 확인하기 때문에 문자열 길이 *2를 해서 확인한다.
'''