#selfnumber = []

def d(n):
    num = list(str(n))
    asw = n
    for i in range(len(num)):
        asw += int(num[i])
    return asw

SET = list(range(1,10001))
for n in range(1,10001):
    if d(n) in SET:
        SET.remove(d(n))

for i in range(len(SET)):
    print(SET[i])


#반복문을 돌려서, 셀프넘버가 아닌 수를 모두 지우고 나머지만 담은 후, 출력하면 되지 않을까?
#근데 이걸 입력받지 않고, 실행하는 방법을 모르겠다.(이 문제는 입력을 받지 않는 문제라서..)
#느낀점 : 함수를 내가 지정하고, 그것을 사용하자

#숫자형을 문자형으로 바꾸는 과정이 생각보다 오래걸림 while문으로 n이 0보다 큰동안 반복, 10으로 나눈 나머지를 asw에 더해주고, n을 10으로 나누면
#몫만 구할 수 있다