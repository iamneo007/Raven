n = 0
sum = 0

while n<5 :
	value =input('enter the value %s ' %(n+1))

	try :
		value = float(value)
		sum = sum + value
		n = n+1

	except ValueError :
		print('Invalid Input : please enter number in int or float thanku!')


print('the sum is %.2f' %sum)

