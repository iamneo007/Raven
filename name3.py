first_name = input('your first name :')
last_name = input('your last name :')

#old style formatting
print('hello %s %s!' % (first_name, last_name))
print('hello {0} {1}!' .format(first_name,last_name))


print('hello {1} {0}!'.format(first_name,last_name))
print('hello {0} {0} {1}!'.format(first_name,last_name))

