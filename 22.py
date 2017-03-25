
def main():
    n = int(input('N = '))

    # Print the series upto n
    print (fib(n))

def fib(n):
    a, b = 0, 1

    while a < n:
        print(a)
        (a, b) = (b, a + b)


main()




