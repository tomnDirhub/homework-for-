numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    cnt = 0
    for dives in range(1, num + 1):
        if num % dives == 0:
            cnt += 1
    if cnt == 2:
        primes.append(num)
    else:
        not_primes.append(num)
print(primes)
print(not_primes)