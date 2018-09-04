"""

Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.

"""


def uni_char(s):

    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True


print(uni_char('abcdsa'))
print(uni_char(''))
print(uni_char('sdfg'))
print(uni_char('aaa'))