def is_prime(num):

    for i in range(2, num):
        if num <= 1:
            return False
        if num % i == 0:
            return False
    return True


print(is_prime(2))
print(is_prime(9))
print(is_prime(5))
print(is_prime(4))

