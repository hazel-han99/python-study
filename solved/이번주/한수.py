'''import sys
input = sys.stdin.readline

n = int(input()) #n 입력받기

cnt = 0
digit = 0 #일의 자리
decimal = 0 #십의 자리
hundred = 0 #백의 자리
thousand = 0 #천의 자리

for i in range(1, n+1):
    if (i < 10): cnt +=1;
    elif (i // 100 != 0):
        digit = i % 10; print(digit);
        decimal = i % 100; print(decimal);
        hundred = i //100; print(hundred);
        if (digit == decimal == hundred): cnt +=1;
    elif (i // 1000 != 0):
        digit = i % 10;
        decimal = i % 100;
        hundred = i % 1000;
        thousand = i // 1000;
        if (digit == decimal == hundred == thousand): cnt +=1;

print(cnt)'''

'''
실버
시간복잡도 : 4천만번의 연산 안에 들어야함. n이 1000이니까 O(n^2 < n^3)
자리수별로 분리가 잘 안된다.. 왜지?
시간제한 : 30분
깨달은 점 : 두자리수를 if문에 넣지 않았고, 100미만은 모두 한수라는 것을 망각했다. 그리고 각 자리수가 같은 것을 세는 것이 아니라,
자리 수의 차가 같은 것을 세야하는데 문제를 제대로 읽지 않은건지 헷갈렸다.. 
'''

def hansu(num):
    count = 0
    for i in range(1, num+1):
        if i<100:
            count += 1
        else:
            num_list = list(map(int, str(i)))
            if num_list[1]-num_list[0] == num_list[2]-num_list[1]:
                count += 1
    return count

if __name__ == "__main__":
    n = int(input())
print(hansu(n))

