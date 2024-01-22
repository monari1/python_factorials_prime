import random

def randint(min, max):
    return random.randint(min, max - 1)

def is_prime(n, factor_p):
    factor_p[0] = 0
    if n <= 1:
        return False  # Not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factor_p[0] = i
            return False  # Not prime
    return True  # Prime

def test_prime():
    factor = [0]  # Using a list to pass a mutable object as a reference
    n = randint(1, 1000)
    print(f"testing n = {n}; ", end="")
    if not is_prime(n, factor):
        print(f"{n} is composite; factor = {factor[0]}", end="")
        if n % factor[0] == 0:
            return True
        else:
            print(f"Fail for is_prime({n}, {factor[0]})")
            return False
    else:
        print(f"{n} is prime; ", end="")
        for i in range(20):
            factor[0] = randint(2, n // 2)
            if n % factor[0] == 0:
                print(f"Fail for is_prime({n}, {factor[0]})")
                return False
        return True

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for p in primes:
    factor = [0]
    if not is_prime(p, factor):
        print(f"Fail for is_prime({p})")
    else:
        print("Pass")

composites = [1, 4, 6, 8, 10, 14, 21, 25, 27, 33]
for c in composites:
    factor = [0]
    if is_prime(c, factor):
        print(f"Fail for is_prime({c})")
    else:
        print(f"{c} is composite; factor = {factor[0]}")

for i in range(10):
    if test_prime():
        print(f"{i}: pass")
    else:
        print(f"{i}: fail")
