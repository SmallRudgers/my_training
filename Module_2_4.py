numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes =[]
primes =[]

for i in numbers:
    counter_len = 0
    counter_primes = 0
    if i > 1:
        while True:
            counter_len += 1
            if i % counter_len == 0:
                counter_primes += 1

            elif counter_primes > 2:
                not_primes.append(i)
                break

            elif counter_len <= i or counter_len == i:
                continue

            elif counter_primes == 2:
                primes.append(i)
                break

print("Primes:", primes)
print("Not Primes:",not_primes)