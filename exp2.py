while True :
	a = float(input('Enter the first number :'))
	b = float(input('Enter the second number :'))

	try:
		result = a / b
		print('Result = {}'.format(result))

	except ZeroDivisionError:
		print('Error : Divison by Zero')

	try_again = input('\n Try Again (Y/N)?')


	if try_again.upper() != 'Y' :
		break

	print()

print('Good byee')