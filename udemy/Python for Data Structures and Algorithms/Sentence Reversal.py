"""

Given a string of words, reverse all the words. For example:

Given:   'This is the best'
Return:  'best the is This'

As part of this exercise you should remove all leading and trailing whitespace.

So that inputs such as:  '  space here'  and 'space here      '
both become:  'here space'

"""

import re


def rev_word(s):

    s = re.sub("^\s+", "", s)
    s = re.sub("\s+$", "", s)
    s = re.sub("\s\s+", " ", s)

    size = len(s)
    arr = {}
    word = []
    i = 0
    j = 0

    while j < size:
        if s[j] != " ":
            word.append(s[j])
        else:
            i += 1
            arr[i] = "".join(word)
            word = []
        if j == size-1:
            i += 1
            arr[i] = "".join(word)
        j += 1

    reverse = []

    for j in sorted(arr, reverse=True):
        reverse.append(arr[j])

    return " ".join(reverse)


print(rev_word(' Hi John,   are you ready to go? '))
print(rev_word('    space before'))
print(rev_word('space after     '))
