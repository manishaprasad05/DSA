# 20. Function to return all prime numbers between two numbers
def prime_between(start, end):
    primes = []

    for n in range(start, end + 1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                primes.append(n)

    return primes


print("Prime numbers:", prime_between(10, 30))
