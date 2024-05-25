import sys
input = sys.stdin.readline

n = ''

while ('#' not in n):
    if (n == ''):
        n = input().split() #입력받아서 공백을 기준으로 분리
    c = n[0] #첫 번째 요소는 문자열로 저장하고,
    s = list(n[1:]) #두 번째 요소~ 리스트로 저장

    cnt = 0

    for i in range(len(s)):
        s[i] = s[i].lower()
        for j in range(len(s[i])):
            if (c in s[i][j]):
                cnt += 1

    print(c, cnt)
    n = input().split()


'''
브론즈
알게된 점 : lower() 함수는 문자단위로는 접근 불가, 문자열로 접근 해야한다
'''