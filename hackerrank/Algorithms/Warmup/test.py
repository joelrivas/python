import math


def find_number(arr, k):

    arr.sort()

    init_point = 0
    end_point = len(arr)-1

    count = 0

    ans = "NO"

    while init_point <= end_point:

        midpoint = math.ceil(init_point + end_point / 2)

        if arr[midpoint] < k:
            init_point = midpoint + 1
        elif arr[midpoint] > k:
            end_point = midpoint - 1
        else:
            ans = "YES"
            return ans

        count += 1

    return ans


res = find_number([2,3,1], 5)
print(res)
