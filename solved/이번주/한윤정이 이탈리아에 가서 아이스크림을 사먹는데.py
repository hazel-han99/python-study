import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

#아이스크림 종류 배열 생성
iceCreams = []

for i in range(1, n+1):
    iceCreams.append(i)

#섞으면 안되는 조합 배열 생성 후 입력받기
dontCombi = []

for _ in range(m):
    dontCombi.append(list(map(int, input().split())))

#아이스크림 3개 선택
tmp = []
selIce = []

for j in range(n):
    for l in range(j+1, n):
        for k in range(l+1, n):
            tmp.append([iceCreams[j], iceCreams[k], iceCreams[l]])

cnt = 0

for a in range (len(tmp)):
    for b in range (len(dontCombi)):
        if(dontCombi[b] not in tmp[a]):
            selIce.append(tmp[a])
            print(selIce)
            cnt +=1
            
print(selIce)
print(cnt)

'''
시간복잡도 : O(n^3)이하
거의 다 풀었는데, 마지막 조합을 확인하는 것을 not in으로 해결할수가 없다

비교부분을 아래와 같이 풀면 해결된다 arr의 경우를 세개를 만들어줘버리는 것.

for i in ice:
    if arr[i[0]][i[1]] or arr[i[0]][i[2]] or arr[i[1]][i[2]]:
        continue
    count += 1
'''
