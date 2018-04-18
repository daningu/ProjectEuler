  primes = [2]
for i in range(0,10000):
    primes.append(next_prime(primes[-1]))
    
print (len(primes), primes[-1])
