
def get_prime(num):
    if num <= 1:
        print('this is 1, this is a prime number: {}'.format(num))
    else:
        for i in range(2, num):
            if (num % i) == 0:
                print('{} = This not a prime number...'.format(num))
                break
        else:
            print('{} = This is a prime number'.format(num))


def get_prime_bool(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def isPrime(num):
    for n in range(2, num):
        if get_prime_bool(n):
            print('prime:',n)


# num = int(input("Please input a number: "))
num = 6
isPrime(num)
# get_prime(num)

