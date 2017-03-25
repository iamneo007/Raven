names = ['John Doe', 'Jane Doe', 'Johnny Turk']
i = 0
total_names = len(names)
print('Users:')

while i < total_names:
    end = ' and\n' if i == names[-2] else '\n'
    print(' - %s' % names[i], end=end)
    i += 1