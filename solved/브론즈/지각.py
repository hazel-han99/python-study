# import sys
# input = sys.stdin.readline
#
# T = int(input()) #경우의 수 입력받기
# d = [] #수업시간을 입력받을 빈 리스트 생성
#
# #수업을 할 수 있는 최대 지각시간을 계산하는 함수 late
# def late(d):
#     for i in range(len(d)):
#         for j in range(d[i+1]):
#             #print(d[i])
#             if((j**2 + j) > d[i]):
#                 print(j-1); continue#지각시간이 수업시간을 넘어서면, 그 전 j, 즉 최대 지각시간 출력, 다음반복 실행
#
# for i in range(T):
#     d.append(int(input())) #수업시간 입력받기
#
# late(d)

T = int(input())
for i in range(T):
    d = int(input())  # 수업시간
    for j in range(10001):
        if j + j**2 > d:
            print(j-1)
            break

#시간복잡도: O(n^2)?
#거의 다 푼것 같은데 반복문에서 문제가 생겼다.
#입력을 다 하고 출력 해야된다고 생각해서 입력시 바로 2중 for문을 사용하지 않고, 함수로 구분한거였는데 이렇게 해도되는지 궁금하다. -> 된다