import math


def Nd(mean, std, x):
    return 0.5 + 0.5 * math.erf((x-mean)/(std * 2**0.5))


print(round(Nd(20, 2, 19.5), 3))
print(abs(round(Nd(20, 2, 20) - Nd(20, 2, 22), 3)))
