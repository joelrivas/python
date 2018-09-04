def aVeryBigSum(n, ar):
    # Complete this function

    suma = 0

    for i in range(n):
        suma += ar[i]

    return suma


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
