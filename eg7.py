names = ['rose','ace','neo','LUFFY']

i = 0
length=len(names)
print('Users:')

while(i<length) :
	end = 'and\n' if i == length -2 else '\n'
	print('- %s' % names[i])
	i+=1