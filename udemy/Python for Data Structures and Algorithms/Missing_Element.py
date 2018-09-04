"""
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and
deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:  finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:  5 is the missing number

"""
import collections

def finder(list1, list2):

    list2 = sorted(list2)

    for i in range(len(list2)):
        if list1[i] != list2[i]:
            print(list1[i])
            return

    print(list2[-1])


def finder2(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)

    d = collections.defaultdict(int)

    for num in list2:
        d[num] += 1

    for num in list1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


a = [1, 2, 3, 4, 5, 6, 7]
b = [3, 7, 2, 1, 4, 6]

#a = [5, 5, 7, 7]
#b = [7, 5, 7]

#print(finder(a, b))
print(finder2(a, b))
