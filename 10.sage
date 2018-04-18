primes = list(primes(1,2*10**6))
primes
primes.append(0)
for i in range(len(primes)-1):
    primes[-1] += primes[i]
print (primes[-1])
