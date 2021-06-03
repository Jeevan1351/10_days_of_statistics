import math
n = int(input())

values = input().split()
numbers = []
for i in values:
    numbers.append(int(i))

mean = sum(numbers)/n
sum_dist_squared = 0
for i in range(n):
    sum_dist_squared += (numbers[i]-mean)*(numbers[i]-mean)

variance = sum_dist_squared/n
standard_deviation = math.sqrt(variance)
print(round(standard_deviation, 1))
