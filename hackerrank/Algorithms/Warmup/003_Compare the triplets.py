
def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function

    a = [a0, a1, a2]
    b = [b0, b1, b2]

    i = 0

    A = 0
    B = 0

    while i < 3:
        if a[i] > b[i]:
            A += 1
            i += 1
        elif a[i] == b[i]:
            i += 1
            pass
        else:
            B += 1
            i += 1

    return A, B


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))