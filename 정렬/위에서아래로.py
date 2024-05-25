arrLimits = int(input())

numbers = []

for i in range(arrLimits) :
    numbers.append(int(input()))

#numbers.sort()
#numbers.reverse()
numbers = sorted(numbers, reverse=True)

for i in numbers :
    print(i, end=' ')