def quartiles(n, nums, f):
    arr = []
    for i in range(n):
        curr = [nums[i]]*f[i]
        arr.extend(curr)
    arr.sort()
    n = sum(f)
    if n % 2 == 0:
        q2 = (arr[n // 2] + arr[n // 2 - 1]) / 2
        if (n / 2) % 2 != 0:
            q1 = arr[n // 4]
            q3 = arr[(3 * n) // 4]
        else:
            q1 = (arr[n // 4] + arr[n // 4 - 1]) / 2
            q3 = (arr[(3 * n) // 4] + arr[(3 * n) // 4 - 1]) / 2
    else:
        q2 = arr[n // 2]
        if ((n-1)//2) % 2 == 0:
            q1 = (arr[n // 4] + arr[n // 4 - 1]) / 2
            q3 = (arr[(3 * n) // 4] + arr[(3 * n) // 4 - 1]) / 2
        else:
            q1 = arr[n // 4]
            q3 = arr[(3 * n) // 4]
    print(round(q3*1.0 - q1, 1))


no = int(input())
values = input().split()
numbers = []
for i in values:
    numbers.append(int(i))  # input values and appended them to a list
values = input().split()
frequencies = []
for i in values:
    frequencies.append(int(i))
quartiles(no, numbers, frequencies)
