line = input().split()

num = int(line[0])
den = int(line[1])

n = int(input())

p = num/den


ans = pow(1-p, n-1)*p
ans += pow(1-p, n-2)*p
ans += pow(1-p, n-3)*p
ans += pow(1-p, n-4)*p
ans += pow(1-p, n-5)*p
print(round(ans, 3))
