a = float(input('First number :'))
b = float(input('second number :'))

try:

	result = a / b
	print('the result is :',result)

except ZeroDivisonError :

	print('ERROR Division by Zero')