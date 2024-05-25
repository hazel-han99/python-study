import sys
input = sys.stdin.readline()

title = '666' #기본 제목 선언

n = input.rstrip() #n번째 수 입력받기

if(n == 1):
    print(title)
else: print(str(int(n) - 1) + title) #n번째 제목 출력

'''
각 자리수를 더할 때, x % 10, x =// 하면 구할 수 있음
'''