scores = [45, 45]

grade = sum(scores) / len(scores)

if 90 <= grade <= 100:
    print('O')
elif 80 <= grade < 90:
    print('E')
elif 70 <= grade < 80:
    print('A')
elif 55 <= grade < 70:
    print('P')
elif 40 <= grade < 50:
    print('D')
elif grade < 40:
    print('T')