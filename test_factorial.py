import random

def randint(min, max):
    return random.randint(min, max - 1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def test_factorial():
    n = randint(1, 25)
    if factorial(n) != n * factorial(n - 1):
        print(f"Fail for factorial({n})")
        return False
    else:
        return True

if factorial(0) != 1:
    print("Fail for factorial(0) == 1")
if factorial(3) != 6:
    print("Fail for factorial(3) == 6")
if factorial(5) != 120:
    print("Fail for factorial(5) == 120")

for i in range(10):
    if test_factorial():
        print(f"{i}: pass")
    else:
        print(f"{i}: fail")
