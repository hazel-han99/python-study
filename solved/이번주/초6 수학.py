'''import sys
input = sys.stdin.readline

case = int(input())

cnt = 0
while (cnt < case):
    n, m = map(int, input().split())

    print(n)
    print(m)

    #최소공배수
    # maxCommon = 0
    # tmpMaxCommonN = []
    # tmpMaxCommonM = []
    #
    # for a in range(1, 1001):
    #     tmpMaxCommonN.append(n * a)
    #     tmpMaxCommonM.append(m * a)
    #     # for b in range(1001):
    #     #
    #     #     for c in range(1001):
    #     if (n == m): maxCommon = n
    #
    # print(maxCommon)

    #최대공약수
    tmpN = []
    tmpM = []

    for i in range(1, n+1):
        if (n % i == 0):
            tmpN.append(i)

    for j in range(1, m+1):
        if (m % j == 0):
            tmpM.append(j)

    minCommon = []

    for k in range(len(tmpN)):
        for l in range(len(tmpM)):
            if (tmpN[k] == tmpM[l]): minCommon.append(tmpN[k])

    print(max(minCommon))

    # print(max(minCommon) + ' ' + maxCommon)
    cnt += 1'''

'''
브론즈
최대공약수를 구하는 방법은 구현했는데, 최소공배수를 구하는 과정에서 비교하는 방법을 완벽히 구현하지 못했다.
시간제한 : 20분
깨달은 점 : 유클리드 호제법이라는 아주 쉬운 방법이 있었다
유클리드 호제법이란,
숫자 a, b가 있을 때, a를 b로 나눈 나머지와 b 의최대 공약수 는 a 와 b 의 최대 공약수 가 같다는 것을 의미한다.
그럼, 계속해서 a 를 b로 나누어서 b를 a에 나눈 나머지를 b 에 대입시켜서 b 가 0이 될때 까지 반복을
하면, 남는 a 값이 바로 최대 공약수 이다.
'''

# 1850 최대공약수
import sys
input = sys.stdin.readline
T = int(input())

def gcd_for(a,b) :
    while b > 0 :
        tmp = a%b
        a = b
        b = tmp
    return a

def gcd_r(a,b) :
    if b == 0 :
        return a
    else :
        return gcd_r(b,a%b)

def lcm(a,b) :
    return a*b//gcd_r(a,b)

for _ in range(T) :
    a, b = map(int,input().split())
    print(lcm(a,b),gcd_r(a,b))


