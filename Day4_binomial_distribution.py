c = [1, 6, 15, 20, 15, 6, 1]
line = input().split()
total = (float(line[0])+float(line[1]))
p = float(line[0]) / total
q = float(line[1])/total

P = c[0]*pow(p, 6) + c[1]*pow(p, 5)*q + c[2]*pow(p, 4)*pow(q, 2) + c[3]*pow(p, 3)*pow(q, 3)
print(round(P, 3))
