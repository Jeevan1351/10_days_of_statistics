def quartiles(n, arr):
    arr.sort()
    # print(arr)
    q1, q2, q3 = 0, 0, 0
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
        q1 = (arr[n // 4] + arr[n // 4 - 1]) / 2
        q3 = (arr[(3 * n) // 4] + arr[(3 * n) // 4 + 1]) / 2

    print(int(q1))
    print(int(q2))
    print(int(q3))


n = int(input())
values = input().split()
numbers = []
for i in values:
    numbers.append(int(i))  # input values and appended them to a list
quartiles(n, numbers)
