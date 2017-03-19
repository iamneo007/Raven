names = ['Nieo', 'anusha' ,'nilesh']

names[0] = 'Foo Bar'
print('names now :',names)

names.append('john watson')
names.append('sherlock holmes')
print('names finally:',names)
print('last name in the list : %s' % names[-1])


joined_names = '\n' .join(names)
print('\nlist of names:')
print(joined_names)
