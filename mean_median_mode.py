n = int(input())
values = input().split()
numbers = []
for i in values:
    numbers.append(int(i))

sumOfNumbers = sum(numbers)
mean = sumOfNumbers/n
numbers.sort()
print(numbers)
# median = 0
# if n%2 == 0:
#     median = (numbers[n//2]+numbers[n//2-1])/2
# else:
#     median = numbers[n//2]
count = 1
i = 1
thisDict = {}
while i < n:
    if numbers[i] == numbers[i-1]:
        count += 1
    else:
        thisDict[numbers[i-1]] = count
        count = 1
    i += 1
thisDict[numbers[-1]] = count
maxi = thisDict[numbers[0]]
print(thisDict)
no = numbers[0]
i = 0
cur = []
while i < n:
    if maxi < thisDict[numbers[i]]:
        no = numbers[i]
        maxi = thisDict[no]
        cur = [no]
    elif maxi == thisDict[numbers[i]]:
        cur.append(numbers[i])
        # print(cur)
    i += 1
mode = min(cur)
print(mean)
# print(median)
print(mode)
