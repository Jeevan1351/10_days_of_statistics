def nc2(n):
    return n*(n-1)/2


line = input().split()
p = int(line[0])/100
no = int(line[1])
P = pow(1-p, no) + no*pow(1-p, no-1)*p + nc2(no)*pow(1-p, no-2)*p*p
print(round(P, 3))
print(round(1-P+nc2(no)*pow(1-p, no-2)*p*p, 3))
