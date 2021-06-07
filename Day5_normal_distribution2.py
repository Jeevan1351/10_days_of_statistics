import math


def Nd(mean, std, x):
    return 0.5 + 0.5 * math.erf((x-mean)/(std * 2**0.5))


print(round((1 - Nd(70, 10, 80))*100, 2))
print((round((1 - Nd(70, 10, 60))*100, 2)))
print(round((Nd(70, 10, 60))*100, 2))

