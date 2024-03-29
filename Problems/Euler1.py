def isPrime(number):
    prime = 0
    if number % 2 == 1:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                prime += 1
        if prime == 0:
            return True
        else:
            return False
    else:
        return False


total = 0
for i in range(1000000, 10000000):
    if isPrime(i):
        total += i

print(total)