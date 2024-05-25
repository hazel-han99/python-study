#아이디어 : 가장 큰 액수부터 나누면, 그것이 최소의 거스름돈 갯수가 된다.

coinArr = [500, 100, 50, 10]

money = int(input()) #금액 입력받기

coinCount = 0 #거스름돈의 개수

#배열의 원소 순서대로 반복
for coin in coinArr :
    coinCount += money // coin
    #money = money % i
    money %= coin
    #if (money == 0) : break #금액이 0원이 되면, 반복문 탈출

print(coinCount)