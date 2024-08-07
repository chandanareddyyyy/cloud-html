def ifprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sep_primes(numbers):
    primes = []
    non_primes = []
    for num in numbers:
        if ifprime(num):
            primes.append(num)
        else:
            non_primes.append(num)
    return primes, non_primes

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Separate prime and non-prime numbers
primes, non_primes = sep_primes(numbers)

# Print results
print("Prime numbers:", primes)
print("Non-prime numbers:", non_primes)
