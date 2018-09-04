"""

Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

"""


def compress(s):

    lng = len(s)
    output = ""
    i = 0

    if lng == 0:
        return ""

    if lng == 1:
        return s+"1"

    while i < lng:
        letter = s[i]
        j = 0
        while i < lng and s[i] == letter:
            i += 1
            j += 1
        output += letter+str(j)

    return output

print(compress(''))
print(compress('J'))
print(compress('AAAAABBBBCCCC'))
print(compress('AABBCC'))
print(compress('AAABCCDDDDD'))
