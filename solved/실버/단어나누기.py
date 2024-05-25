import sys

word = list(map(str, sys.stdin.readline().rstrip("\n")))
res = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        res.append("".join(first + second + third))

print(min(res))

#이 문제는 진짜 아예 모르겠음. 어떻게 무작위로 잘라야하는가에 random()함수를 써야하나도 생각했음