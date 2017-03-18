equation = input('enter the equtaion of the line in the form y=mx+c \n ')

#'y' , 'mx+c'
rhs = equation.split('=')[1]
parts = rhs.split('+')

# 'mx' , 'c'
m = parts[0].replace('x','').strip()
c = parts[1].strip()

#print them out
print('slope of line :{}'.format(m))
print('y-intercept :{}'.format(c))



